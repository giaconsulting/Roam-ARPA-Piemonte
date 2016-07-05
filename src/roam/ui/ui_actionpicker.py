# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_actionpicker.ui'
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

class Ui_ActionPickerDialog(object):
    def setupUi(self, ActionPickerDialog):
        ActionPickerDialog.setObjectName(_fromUtf8("ActionPickerDialog"))
        ActionPickerDialog.resize(808, 152)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ActionPickerDialog.sizePolicy().hasHeightForWidth())
        ActionPickerDialog.setSizePolicy(sizePolicy)
        ActionPickerDialog.setStyleSheet(_fromUtf8(""))
        ActionPickerDialog.setModal(False)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(ActionPickerDialog)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame = QtGui.QFrame(ActionPickerDialog)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
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
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.frame)

        self.retranslateUi(ActionPickerDialog)
        QtCore.QMetaObject.connectSlotsByName(ActionPickerDialog)

    def retranslateUi(self, ActionPickerDialog):
        ActionPickerDialog.setWindowTitle(QtGui.QApplication.translate("ActionPickerDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

