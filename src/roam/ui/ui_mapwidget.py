# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_mapwidget.ui'
#
# Created: Thu Mar 12 14:48:00 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CanvasWidget(object):
    def setupUi(self, CanvasWidget):
        CanvasWidget.setObjectName(_fromUtf8("CanvasWidget"))
        CanvasWidget.resize(800, 644)
        CanvasWidget.setIconSize(QtCore.QSize(48, 48))
        CanvasWidget.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainwidget = QtGui.QWidget(CanvasWidget)
        self.mainwidget.setObjectName(_fromUtf8("mainwidget"))
        self.gridLayout = QtGui.QGridLayout(self.mainwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.canvas = QgsMapCanvas(self.mainwidget)
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        CanvasWidget.setCentralWidget(self.mainwidget)
        self.projecttoolbar = HideableToolbar(CanvasWidget)
        self.projecttoolbar.setMovable(False)
        self.projecttoolbar.setFloatable(False)
        self.projecttoolbar.setObjectName(_fromUtf8("projecttoolbar"))
        CanvasWidget.addToolBar(QtCore.Qt.TopToolBarArea, self.projecttoolbar)
        self.actionHome = QtGui.QAction(CanvasWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/home")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon)
        self.actionHome.setObjectName(_fromUtf8("actionHome"))
        self.actionRaster = QtGui.QAction(CanvasWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/photo")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRaster.setIcon(icon1)
        self.actionRaster.setObjectName(_fromUtf8("actionRaster"))
        self.actionPan = QtGui.QAction(CanvasWidget)
        self.actionPan.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/pan")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon2)
        self.actionPan.setObjectName(_fromUtf8("actionPan"))
        self.actionZoom_In = QtGui.QAction(CanvasWidget)
        self.actionZoom_In.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/in")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon3)
        self.actionZoom_In.setObjectName(_fromUtf8("actionZoom_In"))
        self.actionZoom_Out = QtGui.QAction(CanvasWidget)
        self.actionZoom_Out.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/out")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon4)
        self.actionZoom_Out.setObjectName(_fromUtf8("actionZoom_Out"))
        self.actionInfo = QtGui.QAction(CanvasWidget)
        self.actionInfo.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/select")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInfo.setIcon(icon5)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionAnnotation = QtGui.QAction(CanvasWidget)
        self.actionAnnotation.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/widgets/drawing")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnnotation.setIcon(icon6)
        self.actionAnnotation.setObjectName(_fromUtf8("actionAnnotation"))
        self.actionLayerList = QtGui.QAction(CanvasWidget)
        self.actionLayerList.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/open")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLayerList.setIcon(icon7)
        self.actionLayerList.setObjectName(_fromUtf8("actionLayerList"))
        self.projecttoolbar.addAction(self.actionHome)
        self.projecttoolbar.addAction(self.actionRaster)
        self.projecttoolbar.addAction(self.actionPan)
        self.projecttoolbar.addAction(self.actionZoom_In)
        self.projecttoolbar.addAction(self.actionZoom_Out)
        self.projecttoolbar.addAction(self.actionInfo)
        self.projecttoolbar.addAction(self.actionAnnotation)
        self.projecttoolbar.addAction(self.actionLayerList)

        self.retranslateUi(CanvasWidget)
        QtCore.QMetaObject.connectSlotsByName(CanvasWidget)

    def retranslateUi(self, CanvasWidget):
        CanvasWidget.setWindowTitle(QtGui.QApplication.translate("CanvasWidget", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.projecttoolbar.setWindowTitle(QtGui.QApplication.translate("CanvasWidget", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHome.setText(QtGui.QApplication.translate("CanvasWidget", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRaster.setText(QtGui.QApplication.translate("CanvasWidget", "Imagery", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPan.setText(QtGui.QApplication.translate("CanvasWidget", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setText(QtGui.QApplication.translate("CanvasWidget", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setText(QtGui.QApplication.translate("CanvasWidget", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("CanvasWidget", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnnotation.setText(QtGui.QApplication.translate("CanvasWidget", "Annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLayerList.setText(QtGui.QApplication.translate("CanvasWidget", "Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLayerList.setToolTip(QtGui.QApplication.translate("CanvasWidget", "Active Layer", None, QtGui.QApplication.UnicodeUTF8))

from roam.gui import HideableToolbar
from qgis.gui import QgsMapCanvas
import resources_rc
