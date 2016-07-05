# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_projectwidget.ui'
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
        Form.resize(468, 112)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(20000, 200))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imagelabel = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagelabel.sizePolicy().hasHeightForWidth())
        self.imagelabel.setSizePolicy(sizePolicy)
        self.imagelabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imagelabel.setMaximumSize(QtCore.QSize(200, 200))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setObjectName(_fromUtf8("imagelabel"))
        self.gridLayout.addWidget(self.imagelabel, 0, 0, 2, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.namelabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.namelabel.setFont(font)
        self.namelabel.setStyleSheet(_fromUtf8(""))
        self.namelabel.setWordWrap(True)
        self.namelabel.setProperty(_fromUtf8("projectlabel"), True)
        self.namelabel.setProperty(_fromUtf8("headerlabel"), True)
        self.namelabel.setObjectName(_fromUtf8("namelabel"))
        self.verticalLayout.addWidget(self.namelabel)
        self.descriptionlabel = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.descriptionlabel.setFont(font)
        self.descriptionlabel.setStyleSheet(_fromUtf8(""))
        self.descriptionlabel.setWordWrap(True)
        self.descriptionlabel.setProperty(_fromUtf8("projectlabel"), True)
        self.descriptionlabel.setObjectName(_fromUtf8("descriptionlabel"))
        self.verticalLayout.addWidget(self.descriptionlabel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 2, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 2, 1)
        self.line = QtGui.QFrame(Form)
        self.line.setStyleSheet(_fromUtf8("color: rgb(147, 147, 147);"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 10)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.closeProjectButton = QtGui.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cross_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeProjectButton.setIcon(icon)
        self.closeProjectButton.setIconSize(QtCore.QSize(32, 32))
        self.closeProjectButton.setFlat(True)
        self.closeProjectButton.setObjectName(_fromUtf8("closeProjectButton"))
        self.verticalLayout_2.addWidget(self.closeProjectButton)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.versionlabel = QtGui.QLabel(Form)
        self.versionlabel.setStyleSheet(_fromUtf8(""))
        self.versionlabel.setMargin(6)
        self.versionlabel.setProperty(_fromUtf8("projectlabel"), True)
        self.versionlabel.setObjectName(_fromUtf8("versionlabel"))
        self.verticalLayout_2.addWidget(self.versionlabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 9, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.imagelabel.setText(QtGui.QApplication.translate("Form", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.namelabel.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionlabel.setText(QtGui.QApplication.translate("Form", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.closeProjectButton.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.versionlabel.setText(QtGui.QApplication.translate("Form", "Version", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
