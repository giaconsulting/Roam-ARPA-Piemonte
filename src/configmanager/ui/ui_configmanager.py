# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\configmanager\ui\ui_configmanager.ui'
#
# Created: Thu Mar 12 14:48:04 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProjectInstallerDialog(object):
    def setupUi(self, ProjectInstallerDialog):
        ProjectInstallerDialog.setObjectName(_fromUtf8("ProjectInstallerDialog"))
        ProjectInstallerDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ProjectInstallerDialog.resize(1089, 688)
        ProjectInstallerDialog.setMinimumSize(QtCore.QSize(700, 0))
        ProjectInstallerDialog.setStyleSheet(_fromUtf8("QDialog { \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"        QToolButton { \n"
"            padding: 4px;\n"
"            color: #4f4f4f;\n"
"         }\n"
"\n"
"        QToolButton:hover { \n"
"            padding: 4px;\n"
"            background-color: rgb(211, 228, 255);\n"
"         }"))
        ProjectInstallerDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectInstallerDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mOptionsSplitter = QtGui.QSplitter(ProjectInstallerDialog)
        self.mOptionsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.mOptionsSplitter.setChildrenCollapsible(False)
        self.mOptionsSplitter.setObjectName(_fromUtf8("mOptionsSplitter"))
        self.mOptionsListFrame = QtGui.QFrame(self.mOptionsSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mOptionsListFrame.sizePolicy().hasHeightForWidth())
        self.mOptionsListFrame.setSizePolicy(sizePolicy)
        self.mOptionsListFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.mOptionsListFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.mOptionsListFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mOptionsListFrame.setObjectName(_fromUtf8("mOptionsListFrame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mOptionsListFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.mOptionsListFrame)
        self.frame.setStyleSheet(_fromUtf8("QFrame { \n"
"background-color: rgb(85,85,85);\n"
"}"))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.newProjectButton = QtGui.QPushButton(self.frame)
        self.newProjectButton.setStyleSheet(_fromUtf8("color: white;"))
        self.newProjectButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newProjectButton.setIcon(icon)
        self.newProjectButton.setIconSize(QtCore.QSize(24, 24))
        self.newProjectButton.setFlat(True)
        self.newProjectButton.setObjectName(_fromUtf8("newProjectButton"))
        self.horizontalLayout_2.addWidget(self.newProjectButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.removeProjectButton = QtGui.QPushButton(self.frame)
        self.removeProjectButton.setStyleSheet(_fromUtf8("color: white;"))
        self.removeProjectButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/remove")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeProjectButton.setIcon(icon1)
        self.removeProjectButton.setIconSize(QtCore.QSize(24, 24))
        self.removeProjectButton.setFlat(True)
        self.removeProjectButton.setObjectName(_fromUtf8("removeProjectButton"))
        self.horizontalLayout_2.addWidget(self.removeProjectButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.projectList = QtGui.QTreeView(self.mOptionsListFrame)
        self.projectList.setMinimumSize(QtCore.QSize(58, 0))
        self.projectList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.projectList.setStyleSheet(_fromUtf8("QTreeView {\n"
"    background-color: rgb(85,85,85);\n"
"    outline: 0;\n"
"}\n"
"\n"
"QTreeView::item::selected {\n"
"  background-color:white;\n"
"  color: black;\n"
"  padding-right: 0px;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"  padding: 5px;\n"
"  color: white;\n"
"}\n"
""))
        self.projectList.setFrameShape(QtGui.QFrame.NoFrame)
        self.projectList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.projectList.setAutoScrollMargin(16)
        self.projectList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.projectList.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.projectList.setIconSize(QtCore.QSize(24, 24))
        self.projectList.setTextElideMode(QtCore.Qt.ElideNone)
        self.projectList.setObjectName(_fromUtf8("projectList"))
        self.verticalLayout_2.addWidget(self.projectList)
        self.projectwidget = ProjectWidget(self.mOptionsSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectwidget.sizePolicy().hasHeightForWidth())
        self.projectwidget.setSizePolicy(sizePolicy)
        self.projectwidget.setObjectName(_fromUtf8("projectwidget"))
        self.verticalLayout.addWidget(self.mOptionsSplitter)
        self.mButtonBoxFrame = QtGui.QFrame(ProjectInstallerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mButtonBoxFrame.sizePolicy().hasHeightForWidth())
        self.mButtonBoxFrame.setSizePolicy(sizePolicy)
        self.mButtonBoxFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.mButtonBoxFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mButtonBoxFrame.setObjectName(_fromUtf8("mButtonBoxFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.mButtonBoxFrame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addWidget(self.mButtonBoxFrame)

        self.retranslateUi(ProjectInstallerDialog)
        QtCore.QMetaObject.connectSlotsByName(ProjectInstallerDialog)

    def retranslateUi(self, ProjectInstallerDialog):
        ProjectInstallerDialog.setWindowTitle(QtGui.QApplication.translate("ProjectInstallerDialog", "IntraMaps Config Manager", None, QtGui.QApplication.UnicodeUTF8))

from configmanager.ui.projectwidget import ProjectWidget
import resources_rc
import resources_rc
