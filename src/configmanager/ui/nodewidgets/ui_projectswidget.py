# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\configmanager\ui\nodewidgets\ui_projectswidget.ui'
#
# Created: Thu Mar 12 14:48:05 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_projectsnode(object):
    def setupUi(self, projectsnode):
        projectsnode.setObjectName(_fromUtf8("projectsnode"))
        projectsnode.resize(419, 401)
        self.verticalLayout = QtGui.QVBoxLayout(projectsnode)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_15 = QtGui.QLabel(projectsnode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_11.addWidget(self.label_15)
        self.projectlocations = QtGui.QComboBox(projectsnode)
        self.projectlocations.setObjectName(_fromUtf8("projectlocations"))
        self.horizontalLayout_11.addWidget(self.projectlocations)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.newprojectButton = QtGui.QToolButton(projectsnode)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newprojectButton.setIcon(icon)
        self.newprojectButton.setIconSize(QtCore.QSize(32, 32))
        self.newprojectButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.newprojectButton.setAutoRaise(True)
        self.newprojectButton.setObjectName(_fromUtf8("newprojectButton"))
        self.horizontalLayout_10.addWidget(self.newprojectButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem2 = QtGui.QSpacerItem(20, 240, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(projectsnode)
        QtCore.QMetaObject.connectSlotsByName(projectsnode)

    def retranslateUi(self, projectsnode):
        projectsnode.setWindowTitle(QtGui.QApplication.translate("projectsnode", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("projectsnode", "Projects loaded from:", None, QtGui.QApplication.UnicodeUTF8))
        self.newprojectButton.setText(QtGui.QApplication.translate("projectsnode", "New project", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
