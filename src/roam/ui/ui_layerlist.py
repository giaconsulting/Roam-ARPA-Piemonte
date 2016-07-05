# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_layerlist.ui'
#
# Created: Thu Mar 12 14:47:58 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LayerList(object):
    def setupUi(self, LayerList):
        LayerList.setObjectName(_fromUtf8("LayerList"))
        LayerList.resize(291, 200)
        LayerList.setMinimumSize(QtCore.QSize(291, 200))
        LayerList.setMaximumSize(QtCore.QSize(291, 200))
        LayerList.setAcceptDrops(True)
        self.gridLayout = QtGui.QGridLayout(LayerList)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.LayerListframe = QtGui.QFrame(LayerList)
        self.LayerListframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LayerListframe.setFrameShadow(QtGui.QFrame.Raised)
        self.LayerListframe.setObjectName(_fromUtf8("LayerListframe"))
        self.scrollArea = QtGui.QScrollArea(self.LayerListframe)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 291, 200))
        self.scrollArea.setMinimumSize(QtCore.QSize(291, 200))
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.LayerListwidget = QtGui.QWidget()
        self.LayerListwidget.setGeometry(QtCore.QRect(0, 0, 289, 198))
        self.LayerListwidget.setStyleSheet(_fromUtf8("margin: 5px 0 2px 5px;\n"
"border-style:hidden;"))
        self.LayerListwidget.setObjectName(_fromUtf8("LayerListwidget"))
        self.scrollArea.setWidget(self.LayerListwidget)
        self.gridLayout.addWidget(self.LayerListframe, 0, 0, 1, 1)

        self.retranslateUi(LayerList)
        QtCore.QMetaObject.connectSlotsByName(LayerList)

    def retranslateUi(self, LayerList):
        LayerList.setWindowTitle(QtGui.QApplication.translate("LayerList", "Layer List", None, QtGui.QApplication.UnicodeUTF8))

