from functools import partial
from collections import defaultdict
from subprocess import Popen
import getpass
import traceback
import os
import sys

from PyQt4.QtCore import Qt, QFileInfo, QDir, QSize, QUrl
from PyQt4.QtGui import (QActionGroup, QDesktopServices,
                        QApplication,
                        QWidget,
                        QSizePolicy,
                        QLabel,
                        QApplication,
                        QPixmap,
                        QColor,
                        QStandardItemModel,
                        QStandardItem,
                        QIcon,
                        QComboBox,
                        QAction,
                        QCursor, QFrame, QDesktopServices, QToolButton, QPushButton, QMessageBox, QIcon, QDialog, QGridLayout)
from qgis.core import (QgsProjectBadLayerHandler,
                        QgsPalLabeling,
                        QgsMapLayerRegistry,
                        QgsProject,
                        QgsMapLayer,
                        QgsFeature,
                        QgsFields,
                        QgsGeometry,
                        QgsRectangle, QGis)
from qgis.gui import (QgsMessageBar,
                        QgsMapToolZoom,
                        QgsRubberBand,
                        QgsMapCanvas)
from PyQt4.QtWebKit import QWebView, QWebPage

from roam.dataentrywidget import DataEntryWidget
from roam.listmodulesdialog import ProjectsWidget
from roam.settingswidget import SettingsWidget
from roam.importwidget import ImportWidget
from roam.project import Project, NoMapToolConfigured, ErrorInMapTool
from roam.infodock import InfoDock
from roam.annotationdock import AnnotationDock
from roam.layerlist import LayerList
from roam.syncwidget import SyncWidget
from roam.helpviewdialog import HelpPage
from roam.imageviewerwidget import ImageViewer
from roam.gpswidget import GPSWidget
from roam.api import RoamEvents, GPS, RoamInterface, plugins
from roam.ui import ui_mainwindow
from PyQt4.QtGui import QMainWindow
from roam.gpslogging import GPSLogging

import roam.messagebaritems
import roam.utils
import roam.htmlviewer
import roam.api.featureform
import roam.config
import roam.defaults
import roam.api.utils
import roam.roam_style

from roam.help import contentHelp


def alert(text):
    msgBox=QMessageBox()
    msgBox.setText(text)
    msgBox.setWindowTitle("IntraMaps Roam")
    icon = QIcon(":/icons/info")
    msgBox.setWindowIcon(icon)
    msgBox.exec_()

class BadLayerHandler(QgsProjectBadLayerHandler):
    """
    Handler class for any layers that fail to load when
    opening the project.
    """

    def __init__(self, callback):
        """
            callback - Any bad layers are passed to the callback so it
            can do what it wills with them
        """
        super(BadLayerHandler, self).__init__()
        self.callback = callback
		
    def handleBadLayers(self, domNodes, domDocument):
        layers = [node.namedItem("layername").toElement().text() for node in domNodes]
        self.callback(layers)


class MainWindow(ui_mainwindow.Ui_MainWindow, QMainWindow):
    """
    Main application window
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.menutoolbar.setStyleSheet(roam.roam_style.menubarstyle)
        self.project = None
        self.tracking = GPSLogging(GPS)

        self.canvas_page.set_gps(GPS, self.tracking)

        self.canvas = self.canvas_page.canvas

        roam.defaults.canvas = self.canvas
        self.bar = roam.messagebaritems.MessageBar(self.centralwidget)

        self.actionMap.setVisible(False)
        self.actionLegend.setVisible(False)

        self.menuGroup = QActionGroup(self)
        self.menuGroup.setExclusive(True)
        self.menuGroup.addAction(self.actionMap)
        self.menuGroup.addAction(self.actionDataEntry)
        self.menuGroup.addAction(self.actionLegend)
        self.menuGroup.addAction(self.actionProject)
        self.menuGroup.addAction(self.actionImport)
        self.menuGroup.addAction(self.actionSync)
        self.menuGroup.addAction(self.actionSettings)
        self.menuGroup.addAction(self.actionGPS)
        self.menuGroup.triggered.connect(self.updatePage)

        self.projectbuttons = []
        self.pluginactions = []

        self.actionQuit.triggered.connect(self.exit)
        self.actionHelp.triggered.connect(self.showhelp2)
        self.actionLegend.triggered.connect(self.updatelegend)

        self.projectwidget.requestOpenProject.connect(self.loadProject)
        QgsProject.instance().readProject.connect(self._readProject)

        self.gpswidget.setgps(GPS)
        self.gpswidget.settracking(self.tracking)

        self.actionSettings.toggled.connect(self.settingswidget.populateControls)
        self.actionSettings.toggled.connect(self.settingswidget.readSettings)
        self.settingswidget.settingsupdated.connect(self.settingsupdated)

        self.dataentrywidget = DataEntryWidget(self.canvas, self.bar)
        self.dataentrywidget.lastwidgetremoved.connect(self.dataentryfinished)
        self.widgetpage.layout().addWidget(self.dataentrywidget)

        self.dataentrywidget.rejected.connect(self.formrejected)
        RoamEvents.featuresaved.connect(self.featureSaved)
        RoamEvents.helprequest.connect(self.showhelp)

        self.actionProject.triggered.connect(self.closeAnnotation)

        self.pHelp=os.getcwd()
        help_p = "help\IntraMaps Roam - Help.pdf"
        self.pathHelp=os.path.join(self.pHelp,help_p)
		
        def createSpacer(width=0, height=0):
            widget = QWidget()
            widget.setMinimumWidth(width)
            widget.setMinimumHeight(height)
            return widget



        gpsspacewidget = createSpacer(30)
        sidespacewidget = createSpacer(30)
        sidespacewidget2 = createSpacer(height=20)

        sidespacewidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sidespacewidget2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        def createlabel(text):
            style = """
                QLabel {
                        color: #706565;
                        font: 14px "Calibri" ;
                        }"""
            label = QLabel(text)
            label.setStyleSheet(style)

            return label

        self.projectlabel = createlabel("Project: {project}")
        self.userlabel = createlabel("User: {user}".format(user=getpass.getuser()))
        self.positionlabel = createlabel('')
        self.gpslabel = createlabel("GPS: Not active")
        self.statusbar.addWidget(self.projectlabel)
        self.statusbar.addWidget(self.userlabel)
        spacer = createSpacer()
        spacer2 = createSpacer()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.statusbar.addWidget(spacer)
        self.statusbar.addWidget(self.positionlabel)
        self.statusbar.addWidget(spacer2)
        self.statusbar.addWidget(self.gpslabel)

        self.menutoolbar.insertWidget(self.actionQuit, sidespacewidget2)
        self.spaceraction = self.menutoolbar.insertWidget(self.actionProject, sidespacewidget)

        self.panels = []

        self.centralwidget.layout().addWidget(self.statusbar)

        self.actionGPSFeature.setProperty('dataentry', True)

        self.infodock = InfoDock(self.canvas)
        self.infodock.featureupdated.connect(self.highlightfeature)
        self.infodock.hide()
        self.hidedataentry()
        self.canvas.extentsChanged.connect(self.updatestatuslabel)
        self.annotationdock=AnnotationDock(self.canvas)
        self.annotationdock.hide()
        self.layerlist=LayerList(self.canvas)
        self.layerlist.hide()
        RoamEvents.openimage.connect(self.openimage)
        RoamEvents.openurl.connect(self.viewurl)
        RoamEvents.openfeatureform.connect(self.openForm)
        RoamEvents.openkeyboard.connect(self.openkeyboard)
        RoamEvents.editgeometry_complete.connect(self.on_geometryedit)
        RoamEvents.onShowMessage.connect(self.showUIMessage)
        RoamEvents.selectionchanged.connect(self.showInfoResults)
        RoamEvents.show_widget.connect(self.dataentrywidget.add_widget)
        RoamEvents.closeProject.connect(self.close_project)
        RoamEvents.showAnnotationUi.connect(self.showAnnotationDock)
        RoamEvents.showLayerListUi.connect(self.showLayerList)

        GPS.gpsposition.connect(self.update_gps_label)
        GPS.gpsdisconnected.connect(self.gps_disconnected)

        self.legendpage.showmap.connect(self.showmap)

        self.currentselection = {}

    def showAnnotationDock(self):
        self.annotationdock.show()

    def showLayerList(self,canvaslayers):
        self.layerlist.show(canvaslayers)

    def closeAnnotation(self):
        RoamEvents.closeAnnotation.emit()
        RoamEvents.DestroyLayerList.emit()

    def set_projectbuttons(self, visible):
        for action in self.projectbuttons:
            action.setVisible(visible)

    def loadpages(self, pages):
        def safe_connect(method, to):
            try:
                method.connect(to)
            except AttributeError:
                pass

        for PageClass in pages:
            action = QAction(self.menutoolbar)
            text = PageClass.title.ljust(13)
            action.setIconText(text)
            action.setIcon(QIcon(PageClass.icon))
            action.setCheckable(True)
            if PageClass.projectpage:
                action.setVisible(False)
                self.projectbuttons.append(action)
                self.menutoolbar.insertAction(self.spaceraction, action)
            else:
                self.menutoolbar.insertAction(self.actionProject, action)

            iface = RoamInterface(RoamEvents, GPS, self)
            pagewidget = PageClass(iface, self)

            safe_connect(RoamEvents.selectionchanged, pagewidget.selection_changed)
            safe_connect(RoamEvents.projectloaded, pagewidget.project_loaded)

            pageindex = self.stackedWidget.insertWidget(-1, pagewidget)
            action.setProperty('page', pageindex)
            self.pluginactions.append(action)
            self.menuGroup.addAction(action)

    def showUIMessage(self, label, message, level=QgsMessageBar.INFO, time=0, extra=''):
        self.bar.pushMessage(label, message, level, duration=time, extrainfo=extra)

    def updatelegend(self):
        layers = self.project.legendlayersmapping().values()
        self.legendpage.show(layers)
        #self.legendpage.updatecanvas(self.canvas)

    def update_gps_label(self, position, gpsinfo):
        # Recenter map if we go outside of the 95% of the area
        self.gpslabel.setText("GPS: PDOP {}   HDOP {}    VDOP {}".format(gpsinfo.pdop,
                                                                        gpsinfo.hdop,
                                                                        gpsinfo.vdop))

    def gps_disconnected(self):
        self.gpslabel.setText("GPS Not Active")

    def openkeyboard(self):
        if not roam.config.settings.get('keyboard', True):
            return

        roam.api.utils.open_keyboard()

    def viewurl(self, url):
        """
        Open a URL in Roam
        :param url:
        :return:
        """
        key = url.toString().lstrip('file://')
        try:
            # Hack. Eww fix me.
            data, imagetype = roam.htmlviewer.images[os.path.basename(key)]
            pix = QPixmap()
            if imagetype == 'base64':
                pix.loadFromData(data)
            else:
                pix.load(data)
            self.openimage(pix)
        except KeyError:
            pix = QPixmap()
            pix.load(key)
            if pix.isNull():
                QDesktopServices.openUrl(url)
                return
            self.openimage(pix)

    def openimage(self, pixmap):
        viewer = ImageViewer(self.stackedWidget)
        viewer.resize(self.stackedWidget.size())
        viewer.openimage(pixmap)

    def settingsupdated(self, settings):
        self.show()
        self.canvas_page.settings_updated(settings)

    def updatestatuslabel(self):
        extent = self.canvas.extent()
        self.positionlabel.setText("Map Center: {}".format(extent.center().toString()))

    def on_geometryedit(self, form, feature):
        layer = form.QGISLayer
        self.reloadselection(layer, updated=[feature])

    def handle_removed_features(self, layer, layerid, deleted_feature_ids):
        self.canvas.refresh()
        self.reloadselection(layer, deleted=deleted_feature_ids)

    def reloadselection(self, layer, deleted=[], updated=[]):
        """
        Reload the selection after features have been updated or deleted.
        :param layer:
        :param deleted:
        :param updated:
        :return:
        """
        selectedfeatures = []
        for selection_layer, features in self.currentselection.iteritems():
            if layer.name() == selection_layer.name():
                selectedfeatures = features
                layer = selection_layer
                break

        if not selectedfeatures:
            return

        # Update any features that have changed.
        for updatedfeature in updated:
            oldfeatures = [f for f in selectedfeatures if f.id() == updatedfeature.id()]
            for feature in oldfeatures:
                self.currentselection[layer].remove(feature)
                self.currentselection[layer].append(updatedfeature)

        # Delete any old ones
        for deletedid in deleted:
            oldfeatures = [f for f in selectedfeatures if f.id() == deletedid]
            for feature in oldfeatures:
                self.currentselection[layer].remove(feature)

        RoamEvents.selectionchanged.emit(self.currentselection)

    def highlightfeature(self, layer, feature, features):
        self.canvas_page.highlight_active_selection(layer, feature, features)

    def showmap(self):
        self.actionMap.setVisible(True)
        self.actionLegend.setVisible(True)
        self.actionMap.trigger()

    def hidedataentry(self):
        self.actionDataEntry.setVisible(False)

    def showdataentry(self):
        self.actionDataEntry.setVisible(True)
        self.actionDataEntry.trigger()

    def raiseerror(self, *exinfo):
        info = traceback.format_exception(*exinfo)
        item = self.bar.pushError(QApplication.translate('MainWindowPy','Seems something has gone wrong. Press for more details', None, QApplication.UnicodeUTF8),
                                  info)



    def showhelp(self, parent, url):
        help = HelpPage(parent)
        help.setHelpPage(url)
        help.show()

    def showhelp2(self):
		"""
        def showHTMLReport(title, html, data={}, parent=None):
            dialog = HtmlViewerDialog(title)
            dialog.showHTML(html, data)
            dialog.exec_()

        showHTMLReport("Help",contentHelp)"""
		QDesktopServices.openUrl(QUrl.fromLocalFile(self.pathHelp))

    def dataentryfinished(self):
        self.hidedataentry()
        self.showmap()
        self.cleartempobjects()
        self.infodock.refreshcurrent()

    def featuresdeleted(self, layerid, featureids):
        layer = QgsMapLayerRegistry.instance().mapLayer(layerid)
        self.reloadselection(layer, deleted=featureids)
        self.canvas.refresh()

    def featureSaved(self, *args):
        #self.reloadselection(layer, deleted=[featureid])
        self.canvas.refresh()

    def cleartempobjects(self):
        self.canvas_page.clear_temp_objects()

    def formrejected(self, message, level):
        if message:
            RoamEvents.raisemessage("Form Message", message, level, duration=2)

    def openForm(self, form, feature, editmode, *args):
        """
        Open the form that is assigned to the layer
        """
        self.showdataentry()
        self.dataentrywidget.load_feature_form(feature, form, editmode, *args)

    def editfeaturegeometry(self, form, feature, newgeometry):
        layer = form.QGISLayer
        layer.startEditing()
        feature.setGeometry(newgeometry)
        layer.updateFeature(feature)
        saved = layer.commitChanges()
        map(roam.utils.error, layer.commitErrors())
        self.canvas.refresh()
        RoamEvents.editgeometry_complete.emit(form, feature)

    def addNewFeature(self, form, geometry):
        """
        Add a new new feature to the given layer
        """
        layer = form.QGISLayer

        if layer.geometryType() in [QGis.WKBMultiLineString, QGis.WKBMultiPoint, QGis.WKBMultiPolygon]:
            geometry.convertToMultiType()

        try:
            # TODO: This is a gross hack. We need to move this out into a edit tool with better control.
            form, feature = self.editfeaturestack.pop()
            self.editfeaturegeometry(form, feature, newgeometry=geometry)
            return
        except IndexError:
            pass

        feature = form.new_feature(set_defaults=True)
        feature.setGeometry(geometry)
        self.openForm(form, feature, editmode=False)

    def exit(self):
        """
        Exit the application.
        """
        self.close()

    def showInfoResults(self, results):
        forms = {}
        for layer in results.keys():
            layername = layer.name()
            if not layername in forms:
                forms[layername] = list(self.project.formsforlayer(layername))

        self.currentselection = results
        self.infodock.setResults(results, forms, self.project)
        self.infodock.show()


    def missingLayers(self, layers):
        """
        Called when layers have failed to load from the current project
        """
        roam.utils.warning("Missing layers")
        map(roam.utils.warning, layers)

        missinglayers = roam.messagebaritems.MissingLayerItem(layers,
                                                              parent=self.bar)
        self.bar.pushItem(missinglayers)

    def loadprojects(self, projects):
        """
        Load the given projects into the project
        list
        """
        projects = list(projects)
        self.projectwidget.loadProjectList(projects)
        self.syncwidget.loadprojects(projects)

    def updatePage(self, action):
        """
        Update the current stack page based on the current selected
        action
        """
        page = action.property("page")
        self.stackedWidget.setCurrentIndex(page)

    def show(self):
        """
        Override show method. Handles showing the app in fullscreen
        mode or just maximized
        """
        fullscreen = roam.config.settings.get("fullscreen", False)
        if fullscreen:
            self.showFullScreen()
        else:
            self.showMaximized()

    def viewprojects(self):
        self.stackedWidget.setCurrentIndex(1)

    @roam.utils.timeit
    def _readProject(self, doc):
        """
        readProject is called by QgsProject once the map layer has been
        populated with all the layers
        """
        crs = self.canvas_page.init_qgisproject(doc)

        projectpath = QgsProject.instance().fileName()
        self.project = Project.from_folder(os.path.dirname(projectpath))
        proj=str(self.project.folder)
        dbpath = proj + "/_data/annotation.sqlite"
        self.findAnnotationLayer(proj,dbpath)

        self.projectOpened()
        GPS.crs = crs

    def findAnnotationLayer(self, project_path, dbpath):
        flag=0
        if os.path.isfile(dbpath) == False:
            alert("DB Annotation non trovato, Annotation Tool disattivata")
            flag=1

        elif os.path.isfile(dbpath) == True:
            layerid=["point20150114085613922","line20150114085613640","polygon20150114085614076"]
            layer = QgsMapLayerRegistry.instance()

            for x in layerid:
                if layer.mapLayer(x)==None:
                    alert ("Uno o piu' layer Annotation non presente, Annotation Tool disattivata")
                    flag=1
                    break

        self.CheckAnno(flag)

    def CheckAnno(self,flag):
        if flag == 1:
            RoamEvents.setAnnoDisabled.emit()
        elif flag == 0:
            RoamEvents.setAnnoEnabled.emit()

    @roam.utils.timeit
    def projectOpened(self):
        """
            Called when a new project is opened in QGIS.
        """
        projectpath = QgsProject.instance().fileName()
        self.project = Project.from_folder(os.path.dirname(projectpath))

        self.projectlabel.setText("Project: {}".format(self.project.name))

        # Show panels
        for panel in self.project.getPanels():
            self.mainwindow.addDockWidget(Qt.BottomDockWidgetArea, panel)
            self.panels.append(panel)

        self.clear_plugins()
        self.add_plugins(self.project.enabled_plugins)

        layers = self.project.legendlayersmapping().values()
        #self.legendpage.updateitems(layers)

        gps_loglayer = self.project.gpslog_layer()
        if gps_loglayer:
            self.tracking.enable_logging_on(gps_loglayer)
        else:
            roam.utils.info("No gps_log found for GPS logging")
            self.tracking.clear_logging()

        for layer in roam.api.utils.layers():
            if not layer.type() == QgsMapLayer.VectorLayer:
                continue
            layer.committedFeaturesRemoved.connect(partial(self.handle_removed_features, layer))

        self.canvas_page.project_loaded(self.project)
        self.showmap()
        self.set_projectbuttons(True)
        RoamEvents.projectloaded.emit(self.project)

    def clear_plugins(self):
        self.projectbuttons = []
        self.projectbuttons.append(self.actionMap)
        self.projectbuttons.append(self.actionLegend)
        for action in self.pluginactions:
            # Remove the page widget, because we make it on each load
            widget = self.stackedWidget.widget(action.property("page"))
            self.stackedWidget.removeWidget(widget)
            widget.deleteLater()

            self.menutoolbar.removeAction(action)
        self.pluginactions = []

    def add_plugins(self, pluginnames):
        for name in pluginnames:
            # Get the plugin
            try:
                plugin_mod = plugins.loaded_plugins[name]
            except KeyError:
                continue

            if not hasattr(plugin_mod, 'pages'):
                roam.utils.warning("No pages() function found in {}".format(name))
                continue

            pages = plugin_mod.pages()
            self.loadpages(pages)

    @roam.utils.timeit
    def loadProject(self, project):
        """
        Load a project into the application .
        """
        roam.utils.log(project)
        roam.utils.log(project.name)
        roam.utils.log(project.projectfile)
        roam.utils.log(project.valid)

        (passed, message) = project.onProjectLoad()

        if not passed:
            self.bar.pushMessage("Project load rejected", "Sorry this project couldn't"
                                                          "be loaded.  Click for me details.",
                                 QgsMessageBar.WARNING, extrainfo=message)
            return

        self.actionMap.trigger()

        self.close_project()

        # No idea why we have to set this each time.  Maybe QGIS deletes it for
        # some reason.
        self.badLayerHandler = BadLayerHandler(callback=self.missingLayers)
        QgsProject.instance().setBadLayerHandler(self.badLayerHandler)

        # Project loading screen
        self.stackedWidget.setCurrentIndex(3)
        self.projectloading_label.setText("Project {} Loading".format(project.name))
        pixmap = QPixmap(project.splash)
        w = self.projectimage.width()
        h = self.projectimage.height()
        self.projectimage.setPixmap(pixmap.scaled(w,h, Qt.KeepAspectRatio))
        QApplication.processEvents()

        QDir.setCurrent(os.path.dirname(project.projectfile))
        fileinfo = QFileInfo(project.projectfile)
        QgsProject.instance().read(fileinfo)

    def close_project(self, project=None):
        """
        Close the current open project
        """
        if not project is None and not project == self.project:
            return

        self.tracking.clear_logging()
        self.dataentrywidget.clear()
        self.canvas_page.cleanup()
        QgsMapLayerRegistry.instance().removeAllMapLayers()
        for panel in self.panels:
            self.removeDockWidget(panel)
            del panel
            # Remove all the old buttons

        self.panels = []
        oldproject = self.project
        self.project = None
        self.set_projectbuttons(False)
        self.hidedataentry()
        self.infodock.close()
        RoamEvents.selectioncleared.emit()
        RoamEvents.projectClosed.emit(oldproject)
        self.projectwidget.set_open_project(None)

    def closeEvent(self, event):
        RoamEvents.DestroyLayerList.emit()

class HtmlViewerDialog(QDialog):
    def __init__(self, title, parent=None):
        super(HtmlViewerDialog, self).__init__(parent)
        self.setWindowTitle(title)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.htmlviewer = HtmlViewerWidget(self)
        self.layout().addWidget(self.htmlviewer)

    def showHTML(self, html, data):
        self.htmlviewer.showHTML(html, data)

class HtmlViewerWidget(QWidget):
    def __init__(self, parent):
        super(HtmlViewerWidget, self).__init__(parent)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.view = QWebView()
        self.view.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.layout().addWidget(self.view)

    def showHTML(self, html, data):
        if os.path.isfile(html):
            html = open(html).read()

        html = html.replace(r'\n', '<br>')
        self.view.setHtml(html)
