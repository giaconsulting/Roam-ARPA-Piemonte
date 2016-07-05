# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_sync.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(761, 662)
        Form.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.syncallButton = QtGui.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sync")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.syncallButton.setIcon(icon)
        self.syncallButton.setIconSize(QtCore.QSize(48, 48))
        self.syncallButton.setObjectName(_fromUtf8("syncallButton"))
        self.verticalLayout.addWidget(self.syncallButton)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton = QtGui.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/remove")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(24, 24))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.syncstatus = QtGui.QTextEdit(Form)
        self.syncstatus.setFrameShape(QtGui.QFrame.NoFrame)
        self.syncstatus.setReadOnly(True)
        self.syncstatus.setObjectName(_fromUtf8("syncstatus"))
        self.gridLayout.addWidget(self.syncstatus, 1, 2, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.syncwidgets = QtGui.QWidget()
        self.syncwidgets.setGeometry(QtCore.QRect(0, 0, 375, 572))
        self.syncwidgets.setObjectName(_fromUtf8("syncwidgets"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.syncwidgets)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea.setWidget(self.syncwidgets)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.syncstatus.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.syncallButton.setText(QtGui.QApplication.translate("Form", "Sync All", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
