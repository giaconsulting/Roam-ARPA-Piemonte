# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_deletefeature.ui'
#
# Created: Thu Mar 12 14:47:55 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DeleteFeatureDialog(object):
    def setupUi(self, DeleteFeatureDialog):
        DeleteFeatureDialog.setObjectName(_fromUtf8("DeleteFeatureDialog"))
        DeleteFeatureDialog.resize(808, 137)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteFeatureDialog.sizePolicy().hasHeightForWidth())
        DeleteFeatureDialog.setSizePolicy(sizePolicy)
        DeleteFeatureDialog.setStyleSheet(_fromUtf8(""))
        DeleteFeatureDialog.setModal(False)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(DeleteFeatureDialog)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame = QtGui.QFrame(DeleteFeatureDialog)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.deletelabel = QtGui.QLabel(self.frame)
        self.deletelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deletelabel.setObjectName(_fromUtf8("deletelabel"))
        self.gridLayout.addWidget(self.deletelabel, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelButton = QtGui.QPushButton(self.frame)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.deleteButton = QtGui.QPushButton(self.frame)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.headerlabel = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(17)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.headerlabel.setFont(font)
        self.headerlabel.setStyleSheet(_fromUtf8(""))
        self.headerlabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.headerlabel.setObjectName(_fromUtf8("headerlabel"))
        self.gridLayout.addWidget(self.headerlabel, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(209, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.frame)

        self.retranslateUi(DeleteFeatureDialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("pressed()")), DeleteFeatureDialog.reject)
        QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL(_fromUtf8("pressed()")), DeleteFeatureDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DeleteFeatureDialog)

    def retranslateUi(self, DeleteFeatureDialog):
        DeleteFeatureDialog.setWindowTitle(QtGui.QApplication.translate("DeleteFeatureDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.deletelabel.setText(QtGui.QApplication.translate("DeleteFeatureDialog", "Do you really want to delete this feature?", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("DeleteFeatureDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("DeleteFeatureDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.headerlabel.setText(QtGui.QApplication.translate("DeleteFeatureDialog", "Delete feature?", None, QtGui.QApplication.UnicodeUTF8))

