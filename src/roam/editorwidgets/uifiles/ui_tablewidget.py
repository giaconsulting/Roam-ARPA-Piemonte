# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\editorwidgets\uifiles\ui_tablewidget.ui'
#
# Created: Thu Mar 12 14:47:53 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_tablewidget(object):
    def setupUi(self, tablewidget):
        tablewidget.setObjectName(_fromUtf8("tablewidget"))
        tablewidget.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tablewidget.sizePolicy().hasHeightForWidth())
        tablewidget.setSizePolicy(sizePolicy)
        tablewidget.setMinimumSize(QtCore.QSize(0, 300))
        self.gridLayout = QtGui.QGridLayout(tablewidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton = QtGui.QPushButton(tablewidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtGui.QPushButton(tablewidget)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.horizontalLayout.addWidget(self.editButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.table = QtGui.QTableView(tablewidget)
        self.table.setMinimumSize(QtCore.QSize(0, 0))
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setGridStyle(QtCore.Qt.DashLine)
        self.table.setCornerButtonEnabled(False)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        self.retranslateUi(tablewidget)
        QtCore.QMetaObject.connectSlotsByName(tablewidget)

    def retranslateUi(self, tablewidget):
        tablewidget.setWindowTitle(QtGui.QApplication.translate("tablewidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("tablewidget", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("tablewidget", "Edit", None, QtGui.QApplication.UnicodeUTF8))

