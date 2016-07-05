# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\project_installer\ui_installer.ui'
#
# Created: Thu Mar 12 14:48:01 2015
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
        ProjectInstallerDialog.resize(749, 529)
        ProjectInstallerDialog.setMinimumSize(QtCore.QSize(700, 0))
        self.verticalLayout = QtGui.QVBoxLayout(ProjectInstallerDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 3, 0, 0)
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
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mOptionsListWidget = QtGui.QListWidget(self.mOptionsListFrame)
        self.mOptionsListWidget.setMinimumSize(QtCore.QSize(58, 0))
        self.mOptionsListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mOptionsListWidget.setStyleSheet(_fromUtf8("QListWidget {\n"
"    background-color: rgb(85,85,85);\n"
"    padding: 4px;\n"
"    color: white;\n"
"}\n"
"\n"
"QListWidget::item::selected {\n"
"  background-color:palette(Window);\n"
"  color: black;\n"
"}\n"
""))
        self.mOptionsListWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.mOptionsListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mOptionsListWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.mOptionsListWidget.setIconSize(QtCore.QSize(32, 32))
        self.mOptionsListWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.mOptionsListWidget.setResizeMode(QtGui.QListView.Adjust)
        self.mOptionsListWidget.setWordWrap(True)
        self.mOptionsListWidget.setObjectName(_fromUtf8("mOptionsListWidget"))
        QtGui.QListWidgetItem(self.mOptionsListWidget)
        self.verticalLayout_2.addWidget(self.mOptionsListWidget)
        self.mOptionsFrame = QtGui.QFrame(self.mOptionsSplitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mOptionsFrame.sizePolicy().hasHeightForWidth())
        self.mOptionsFrame.setSizePolicy(sizePolicy)
        self.mOptionsFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.mOptionsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mOptionsFrame.setObjectName(_fromUtf8("mOptionsFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mOptionsFrame)
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mOptionsStackedWidget = QtGui.QStackedWidget(self.mOptionsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mOptionsStackedWidget.sizePolicy().hasHeightForWidth())
        self.mOptionsStackedWidget.setSizePolicy(sizePolicy)
        self.mOptionsStackedWidget.setObjectName(_fromUtf8("mOptionsStackedWidget"))
        self.mOptsPage_01 = QtGui.QWidget()
        self.mOptsPage_01.setObjectName(_fromUtf8("mOptsPage_01"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.mOptsPage_01)
        self.verticalLayout_14.setMargin(0)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label = QtGui.QLabel(self.mOptsPage_01)
        self.label.setStyleSheet(_fromUtf8("font-weight:bold;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_14.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea(self.mOptsPage_01)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 488, 475))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_13.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_14.addWidget(self.scrollArea)
        self.mOptionsStackedWidget.addWidget(self.mOptsPage_01)
        self.verticalLayout_3.addWidget(self.mOptionsStackedWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self.mOptionsFrame)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)
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
        self.mOptionsStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.mOptionsListWidget, QtCore.SIGNAL(_fromUtf8("currentRowChanged(int)")), self.mOptionsStackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ProjectInstallerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ProjectInstallerDialog)

    def retranslateUi(self, ProjectInstallerDialog):
        ProjectInstallerDialog.setWindowTitle(QtGui.QApplication.translate("ProjectInstallerDialog", "Options Dialog Template", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.mOptionsListWidget.isSortingEnabled()
        self.mOptionsListWidget.setSortingEnabled(False)
        self.mOptionsListWidget.item(0).setText(QtGui.QApplication.translate("ProjectInstallerDialog", "Project Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.mOptionsListWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("ProjectInstallerDialog", "Project Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ProjectInstallerDialog", "Update all project values", None, QtGui.QApplication.UnicodeUTF8))

