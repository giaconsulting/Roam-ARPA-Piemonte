from PyQt4.QtCore import Qt, QSize, QPoint, pyqtSignal
from PyQt4.QtGui import  QWidget, QPixmap, QLabel, QGridLayout
from qgis.core import QgsMapLayer, QGis, QgsMapLayerRegistry
from ui.ui_legend import Ui_legendsWidget
from PyQt4 import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

ICON_SIZE = QSize(30, 30)
HALLIGNEMENT = Qt.AlignCenter

class LegendWidget(Ui_legendsWidget, QWidget):
    showmap = pyqtSignal()

    def __init__(self, parent=None):
        super(LegendWidget, self).__init__(parent)
        self.setupUi(self)
        self.gridLayout = QGridLayout(self.legendList)
        self.gridLayout.setColumnStretch(0,10)
        self.gridLayout.setColumnStretch(1,300)

    def show(self,layers):
        self.dstroyLegend()
        super(LegendWidget, self).show()
        self.items = {}
        for layer in layers:
            if not layer.type() == QgsMapLayer.VectorLayer:
                continue

            try:
                items = layer.rendererV2().legendSymbologyItems(ICON_SIZE)
            except AttributeError:
                continue
            self.items[layer.name()] = items
        self.styleLegend(items)

    def styleLegend(self,items):
        i=0
        for layer, items in self.items.iteritems():
            for text, icon in items:
                if not text or text.startswith("~"):
                    continue
                self.makeLabel(text,icon,i)
                i += 1

    def makeLabel(self,text,icon,nrow):
        self.newLabel=QLabel()
        self.newLabel.setText(text)
        self.newLabel.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.newLabel.setAutoFillBackground(True)
        self.newIcon=QLabel()
        self.newIcon.setPixmap(icon)
        self.newIcon.setStyleSheet(_fromUtf8("background-color:transparent;"))
        self.newIcon.setAutoFillBackground(True)
        self.gridLayout.addWidget(self.newIcon,nrow,0,HALLIGNEMENT)
        self.gridLayout.addWidget(self.newLabel,nrow,1)


    def makeLabelLayer(self,text,nrow):
        self.newLabel=QLabel()
        self.newLabel.setText(text)
        self.gridLayout.addWidget(self.newLabel,nrow,1)

    def dstroyLegend(self):
        while self.gridLayout.count():
            self.item = self.gridLayout.itemAt(0).widget()
            self.gridLayout.removeWidget(self.item)
            self.item.deleteLater()
