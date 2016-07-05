# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_mainwindow.ui'
#
# Created: Thu Mar 12 14:47:59 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(833, 643)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/branding/logo")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet(_fromUtf8(""))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.canvas_page = MapWidget()
        self.canvas_page.setStyleSheet(_fromUtf8(""))
        self.canvas_page.setObjectName(_fromUtf8("canvas_page"))
        self.stackedWidget.addWidget(self.canvas_page)
        self.projectwidget = ProjectsWidget()
        self.projectwidget.setStyleSheet(_fromUtf8(""))
        self.projectwidget.setObjectName(_fromUtf8("projectwidget"))
        self.stackedWidget.addWidget(self.projectwidget)
        self.settingswidget = SettingsWidget()
        self.settingswidget.setStyleSheet(_fromUtf8(""))
        self.settingswidget.setObjectName(_fromUtf8("settingswidget"))
        self.stackedWidget.addWidget(self.settingswidget)
        self.loadin_page = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadin_page.sizePolicy().hasHeightForWidth())
        self.loadin_page.setSizePolicy(sizePolicy)
        self.loadin_page.setObjectName(_fromUtf8("loadin_page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.loadin_page)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.projectimage = QtGui.QLabel(self.loadin_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectimage.sizePolicy().hasHeightForWidth())
        self.projectimage.setSizePolicy(sizePolicy)
        self.projectimage.setText(_fromUtf8(""))
        self.projectimage.setScaledContents(False)
        self.projectimage.setAlignment(QtCore.Qt.AlignCenter)
        self.projectimage.setObjectName(_fromUtf8("projectimage"))
        self.verticalLayout.addWidget(self.projectimage)
        self.projectloading_label = QtGui.QLabel(self.loadin_page)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.projectloading_label.setFont(font)
        self.projectloading_label.setStyleSheet(_fromUtf8(""))
        self.projectloading_label.setScaledContents(True)
        self.projectloading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.projectloading_label.setObjectName(_fromUtf8("projectloading_label"))
        self.verticalLayout.addWidget(self.projectloading_label)
        self.label_2 = QtGui.QLabel(self.loadin_page)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.loadin_page)
        self.widgetpage = QtGui.QWidget()
        self.widgetpage.setStyleSheet(_fromUtf8(""))
        self.widgetpage.setObjectName(_fromUtf8("widgetpage"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widgetpage)
        self.gridLayout_5.setContentsMargins(3, 0, 3, 0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.stackedWidget.addWidget(self.widgetpage)
        self.syncwidget = SyncWidget()
        self.syncwidget.setObjectName(_fromUtf8("syncwidget"))
        self.stackedWidget.addWidget(self.syncwidget)
        self.gpswidget = GPSWidget()
        self.gpswidget.setObjectName(_fromUtf8("gpswidget"))
        self.stackedWidget.addWidget(self.gpswidget)
        self.legendpage = LegendWidget()
        self.legendpage.setObjectName(_fromUtf8("legendpage"))
        self.stackedWidget.addWidget(self.legendpage)
        self.importwidget = ImportWidget()
        self.importwidget.setStyleSheet(_fromUtf8(""))
        self.importwidget.setObjectName(_fromUtf8("importwidget"))
        self.stackedWidget.addWidget(self.importwidget)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menutoolbar = HideableToolbar(MainWindow)
        self.menutoolbar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.menutoolbar.setStyleSheet(_fromUtf8(""))
        self.menutoolbar.setMovable(False)
        self.menutoolbar.setIconSize(QtCore.QSize(48, 48))
        self.menutoolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.menutoolbar.setFloatable(False)
        self.menutoolbar.setProperty(_fromUtf8("page"), 5)
        self.menutoolbar.setObjectName(_fromUtf8("menutoolbar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.menutoolbar)
        self.actionMap = QtGui.QAction(MainWindow)
        self.actionMap.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/map")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMap.setIcon(icon1)
        self.actionMap.setProperty(_fromUtf8("page"), 0)
        self.actionMap.setObjectName(_fromUtf8("actionMap"))
        self.actionProject = QtGui.QAction(MainWindow)
        self.actionProject.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/open")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProject.setIcon(icon2)
        self.actionProject.setProperty(_fromUtf8("page"), 1)
        self.actionProject.setObjectName(_fromUtf8("actionProject"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/config")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setProperty(_fromUtf8("page"), 2)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/quit")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHome = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/home")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon5)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionPan = QtGui.QAction(MainWindow)
        self.actionPan.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pan")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon6)
        self.actionPan.setObjectName(_fromUtf8("actionPan"))
        self.actionZoom_In = QtGui.QAction(MainWindow)
        self.actionZoom_In.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/in")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon7)
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        self.actionZoom_Out.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/out")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon8)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionRaster = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/photo")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRaster.setIcon(icon9)
        self.actionRaster.setObjectName(_fromUtf8("actionRaster"))
        self.actionEdit_Tools = QtGui.QAction(MainWindow)
        self.actionEdit_Tools.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/edittools")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Tools.setIcon(icon10)
        self.actionEdit_Tools.setObjectName(_fromUtf8("actionEdit_Tools"))
        self.actionEdit_Attributes = QtGui.QAction(MainWindow)
        self.actionEdit_Attributes.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/edit")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Attributes.setIcon(icon11)
        self.actionEdit_Attributes.setObjectName(_fromUtf8("actionEdit_Attributes"))
        self.actionEnable_GPS = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gps")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnable_GPS.setIcon(icon12)
        self.actionEnable_GPS.setObjectName(_fromUtf8("actionEnable_GPS"))
        self.actionSync = QtGui.QAction(MainWindow)
        self.actionSync.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sync")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSync.setIcon(icon13)
        self.actionSync.setProperty(_fromUtf8("page"), 5)
        self.actionSync.setObjectName(_fromUtf8("actionSync"))
        self.actionMove = QtGui.QAction(MainWindow)
        self.actionMove.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/move")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove.setIcon(icon14)
        self.actionMove.setObjectName(_fromUtf8("actionMove"))
        self.actionGPSFeature = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/gpsadd")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGPSFeature.setIcon(icon15)
        self.actionGPSFeature.setObjectName(_fromUtf8("actionGPSFeature"))
        self.actionDataEntry = QtGui.QAction(MainWindow)
        self.actionDataEntry.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dataentry")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDataEntry.setIcon(icon16)
        self.actionDataEntry.setProperty(_fromUtf8("page"), 4)
        self.actionDataEntry.setObjectName(_fromUtf8("actionDataEntry"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/info")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInfo.setIcon(icon17)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionGPS = QtGui.QAction(MainWindow)
        self.actionGPS.setCheckable(True)
        self.actionGPS.setIcon(icon12)
        self.actionGPS.setProperty(_fromUtf8("page"), 6)
        self.actionGPS.setObjectName(_fromUtf8("actionGPS"))
        self.actionLegend = QtGui.QAction(MainWindow)
        self.actionLegend.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/legend")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLegend.setIcon(icon18)
        self.actionLegend.setProperty(_fromUtf8("page"), 7)
        self.actionLegend.setObjectName(_fromUtf8("actionLegend"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/import")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon19)
        self.actionImport.setProperty(_fromUtf8("page"), 8)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionHelp = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/help")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon20)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menutoolbar.addAction(self.actionMap)
        self.menutoolbar.addAction(self.actionDataEntry)
        self.menutoolbar.addAction(self.actionLegend)
        self.menutoolbar.addAction(self.actionProject)
        self.menutoolbar.addAction(self.actionImport)
        self.menutoolbar.addAction(self.actionSync)
        self.menutoolbar.addAction(self.actionGPS)
        self.menutoolbar.addAction(self.actionSettings)
        self.menutoolbar.addAction(self.actionHelp)
        self.menutoolbar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "IntraMaps Roam: Mobile Data Collection", None, QtGui.QApplication.UnicodeUTF8))
        self.projectloading_label.setText(QtGui.QApplication.translate("MainWindow", "Project {} Loading", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Please wait....", None, QtGui.QApplication.UnicodeUTF8))
        self.menutoolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "sidetoolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMap.setText(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMap.setIconText(QtGui.QApplication.translate("MainWindow", "Map          ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProject.setText(QtGui.QApplication.translate("MainWindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProject.setIconText(QtGui.QApplication.translate("MainWindow", "Projects    ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setIconText(QtGui.QApplication.translate("MainWindow", "Settings     ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setIconText(QtGui.QApplication.translate("MainWindow", "Quit         ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setText(QtGui.QApplication.translate("MainWindow", "Home View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setToolTip(QtGui.QApplication.translate("MainWindow", "Home View", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPan.setText(QtGui.QApplication.translate("MainWindow", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRaster.setText(QtGui.QApplication.translate("MainWindow", "Aerial Photo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Tools.setText(QtGui.QApplication.translate("MainWindow", "Edit Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Attributes.setText(QtGui.QApplication.translate("MainWindow", "Edit Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnable_GPS.setText(QtGui.QApplication.translate("MainWindow", "Enable GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSync.setText(QtGui.QApplication.translate("MainWindow", "Sync     ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSync.setIconText(QtGui.QApplication.translate("MainWindow", "Sync          ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove.setText(QtGui.QApplication.translate("MainWindow", "Move Feature", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGPSFeature.setText(QtGui.QApplication.translate("MainWindow", "Capture at GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGPSFeature.setToolTip(QtGui.QApplication.translate("MainWindow", "Capture at GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDataEntry.setText(QtGui.QApplication.translate("MainWindow", "Data Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDataEntry.setIconText(QtGui.QApplication.translate("MainWindow", "Data Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGPS.setText(QtGui.QApplication.translate("MainWindow", "GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGPS.setIconText(QtGui.QApplication.translate("MainWindow", "GPS           ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLegend.setText(QtGui.QApplication.translate("MainWindow", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLegend.setIconText(QtGui.QApplication.translate("MainWindow", "Legend      ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setIconText(QtGui.QApplication.translate("MainWindow", "Import      ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setIconText(QtGui.QApplication.translate("MainWindow", "Help           ", None, QtGui.QApplication.UnicodeUTF8))

from roam.gui import ImportWidget, GPSWidget, HideableToolbar, SettingsWidget, SyncWidget, ProjectsWidget, MapWidget, LegendWidget
import resources_rc