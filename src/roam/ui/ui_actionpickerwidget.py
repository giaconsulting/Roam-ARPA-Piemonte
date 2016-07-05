# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_actionpickerwidget.ui'
#
# Created: Thu Mar 12 14:47:54 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_actionpicker(object):
    def setupUi(self, actionpicker):
        actionpicker.setObjectName(_fromUtf8("actionpicker"))
        actionpicker.resize(859, 121)
        self.verticalLayout = QtGui.QVBoxLayout(actionpicker)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(actionpicker)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.actionsLayout = QtGui.QHBoxLayout()
        self.actionsLayout.setContentsMargins(-1, -1, 0, -1)
        self.actionsLayout.setObjectName(_fromUtf8("actionsLayout"))
        self.gridLayout.addLayout(self.actionsLayout, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setProperty(_fromUtf8("headerlabel"), True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(actionpicker)
        QtCore.QMetaObject.connectSlotsByName(actionpicker)

    def retranslateUi(self, actionpicker):
        actionpicker.setWindowTitle(QtGui.QApplication.translate("actionpicker", "Form", None, QtGui.QApplication.UnicodeUTF8))

