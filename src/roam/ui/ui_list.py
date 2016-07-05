# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_list.ui'
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

class Ui_BigList(object):
    def setupUi(self, BigList):
        BigList.setObjectName(_fromUtf8("BigList"))
        BigList.resize(400, 693)
        BigList.setStyleSheet(_fromUtf8("* {\n"
"    font: 75 14pt \"Calibri\";\n"
"}\n"
"\n"
"QLabel[header=\"true\"] {\n"
"    font: 75 20pt \"Calibri\";\n"
"}\n"
"\n"
"QListView::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid rgba(208, 208, 208, 50);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    padding: 8px;\n"
"    color: rgb(85, 85, 255);\n"
"    border-bottom: 1px solid rgba(208, 208, 208, 50);\n"
"}\n"
""))
        self.gridLayout = QtGui.QGridLayout(BigList)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(BigList)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fieldnameLabel = QtGui.QLabel(self.frame)
        self.fieldnameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fieldnameLabel.setProperty(_fromUtf8("header"), True)
        self.fieldnameLabel.setObjectName(_fromUtf8("fieldnameLabel"))
        self.horizontalLayout.addWidget(self.fieldnameLabel)
        self.closebutton = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebutton.sizePolicy().hasHeightForWidth())
        self.closebutton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/widgets/cancel")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setIconSize(QtCore.QSize(48, 48))
        self.closebutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.closebutton.setAutoRaise(True)
        self.closebutton.setObjectName(_fromUtf8("closebutton"))
        self.horizontalLayout.addWidget(self.closebutton)
        self.saveButton = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QtCore.QSize(48, 48))
        self.saveButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.saveButton.setAutoRaise(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.search = QgsFilterLineEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setMinimumSize(QtCore.QSize(0, 40))
        self.search.setStyleSheet(_fromUtf8("background-color: rgb(217, 217, 217);"))
        self.search.setFrame(False)
        self.search.setObjectName(_fromUtf8("search"))
        self.verticalLayout.addWidget(self.search)
        self.listView = QtGui.QListView(self.frame)
        self.listView.setStyleSheet(_fromUtf8("QListView::indicator\n"
"{\n"
"width: 60px;\n"
"height:60px;\n"
"}\n"
"\n"
"QListView::item\n"
"{\n"
"    padding: 20px;\n"
"};\n"
""))
        self.listView.setFrameShape(QtGui.QFrame.NoFrame)
        self.listView.setLineWidth(3)
        self.listView.setIconSize(QtCore.QSize(32, 32))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(BigList)
        QtCore.QMetaObject.connectSlotsByName(BigList)

    def retranslateUi(self, BigList):
        BigList.setWindowTitle(QtGui.QApplication.translate("BigList", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.fieldnameLabel.setText(QtGui.QApplication.translate("BigList", "{field Name}", None, QtGui.QApplication.UnicodeUTF8))
        self.closebutton.setText(QtGui.QApplication.translate("BigList", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("BigList", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.search.setPlaceholderText(QtGui.QApplication.translate("BigList", "Search", None, QtGui.QApplication.UnicodeUTF8))

from qgis.gui import QgsFilterLineEdit
import resources_rc
