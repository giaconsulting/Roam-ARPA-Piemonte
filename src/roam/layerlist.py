from PyQt4.QtGui import QDialog, QWidget, QPixmap, QLabel, QGridLayout
from PyQt4.QtCore import Qt, QSize, QPoint, pyqtSignal
from roam.flickwidget import FlickCharm
from roam.api.events import RoamEvents
from roam.ui.uifiles import (layerlist_widget, layerlist_base)
from PyQt4 import QtGui, QtCore
from qgis.core import QgsMapLayerRegistry
from PyQt4.QtXml import QDomDocument
import glob
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class LayerList(layerlist_widget, layerlist_base):
    def __init__(self,canvas, startimage=None):
        super(LayerList, self).__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.gridLayout = QtGui.QGridLayout(self.LayerListwidget)
        self.gridLayout.setMargin(0)
        self.canvas=canvas
        self.checkbuttons=[]
        super(LayerList, self).finished.connect(self.chiudi)
        RoamEvents.DestroyLayerList.connect(self.destroy)

    def show(self,canvaslayerslist):
        if (super(LayerList, self).isVisible()) == False:
            if len(self.checkbuttons)>0:
                super(LayerList, self).show()
            else:
                super(LayerList, self).show()
                self.canvaslayers = canvaslayerslist
                self.start()
        else:
            self.chiudi()

    def start(self):
        self.deleteCheck()
        self.registry=QgsMapLayerRegistry.instance()
        count=self.registry.count()
        self.checkbuttons=[self.createCheck(self.registry) for x in range (0,count)]

    def destroy(self):
        if len(self.checkbuttons)>0:
            for check in self.checkbuttons:
                check.deleteLater()

            self.deleteCheck()
        super(LayerList, self).hide()
        RoamEvents.closeLayerList.emit()

    def chiudi(self):
        super(LayerList, self).hide()
        RoamEvents.closeLayerList.emit()

    def readXML(self,n):
        filename=glob.glob('*.qgs')
        xml = open(filename[0]).read()
        doc = QDomDocument()
        doc.setContent(xml)
        filelist = doc.elementsByTagName("legendlayerfile")
        layerfile = filelist.at(n).toElement()
        layerid = layerfile.attribute('layerid')
        visible = int(layerfile.attribute('visible'))
        return layerid, bool(visible)

    def createCheck(self,registry):
        layer_id,visible=self.readXML(self.n)
        name=registry.mapLayer(layer_id).name()
        self.layers.update({name:layer_id})
        self.newCheckbox = QtGui.QCheckBox(name,self.LayerListwidget)
        self.newCheckbox.setStyleSheet(_fromUtf8("QCheckBox{font: 11pt \"Arial\";margin-bottom:3px;}\n""QCheckBox:indicator {width: 15px; height: 15px; }"))
        self.gridLayout.addWidget(self.newCheckbox)
        self.newCheckbox.setChecked(visible)
        self.newCheckbox.stateChanged.connect(self.setVisibility)
        self.n += 1
        return self.newCheckbox

    def deleteCheck(self):
        self.layers={}
        self.n=0
        self.checkbuttons=[]

    def setVisibility(self):
        check=self.sender()
        layer_id=self.layers[check.text()]
        maplayer=self.registry.mapLayer(layer_id)

        for layer in self.canvaslayers:
            if layer.layer() == maplayer:
                layer.setVisible(not layer.isVisible())
                self.canvas.setLayerSet(self.canvaslayers)
                self.canvas.freeze(False)
                self.canvas.refresh()
