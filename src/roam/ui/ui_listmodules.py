# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_listmodules.ui'
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

class Ui_ListModules(object):
    def setupUi(self, ListModules):
        ListModules.setObjectName(_fromUtf8("ListModules"))
        ListModules.setWindowModality(QtCore.Qt.NonModal)
        ListModules.resize(813, 473)
        ListModules.setWindowOpacity(1.0)
        ListModules.setAutoFillBackground(False)
        ListModules.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(ListModules)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.moduleList = QtGui.QListWidget(ListModules)
        self.moduleList.setStyleSheet(_fromUtf8(""))
        self.moduleList.setFrameShape(QtGui.QFrame.NoFrame)
        self.moduleList.setObjectName(_fromUtf8("moduleList"))
        self.gridLayout.addWidget(self.moduleList, 1, 0, 1, 1)

        self.retranslateUi(ListModules)
        QtCore.QMetaObject.connectSlotsByName(ListModules)

    def retranslateUi(self, ListModules):
        ListModules.setWindowTitle(QtGui.QApplication.translate("ListModules", "Select form to open", None, QtGui.QApplication.UnicodeUTF8))

