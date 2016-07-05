# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_import.ui'
#
# Created: Thu Mar 12 14:47:57 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_importWidget(object):
    def setupUi(self, importWidget):
        importWidget.setObjectName(_fromUtf8("importWidget"))
        importWidget.resize(848, 786)
        importWidget.setAutoFillBackground(False)
        importWidget.setStyleSheet(_fromUtf8("QLabel#settingsLabel {\n"
"    color: #4f4f4f;\n"
"    font: 25pt \"Segoe UI\" ;\n"
"}\n"
"\n"
"    * {\n"
"            font: 20px \"Segoe UI\" ;\n"
"        }    "))
        self.gridLayout = QtGui.QGridLayout(importWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(importWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(importWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(importWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.label = QtGui.QLabel(importWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 2, 1, 1)

        self.retranslateUi(importWidget)
        QtCore.QMetaObject.connectSlotsByName(importWidget)

    def retranslateUi(self, importWidget):
        importWidget.setWindowTitle(QtGui.QApplication.translate("importWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("importWidget", "Select project\'s path", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("importWidget", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("importWidget", "Import project path", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
import resources_rc
import resources_rc
