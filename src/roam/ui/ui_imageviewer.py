# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_imageviewer.ui'
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

class Ui_imageviewer(object):
    def setupUi(self, imageviewer):
        imageviewer.setObjectName(_fromUtf8("imageviewer"))
        imageviewer.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(imageviewer)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(imageviewer)
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnOpenImage = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenImage.sizePolicy().hasHeightForWidth())
        self.btnOpenImage.setSizePolicy(sizePolicy)
        self.btnOpenImage.setIconSize(QtCore.QSize(32, 32))
        self.btnOpenImage.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.btnOpenImage.setAutoRaise(True)
        self.btnOpenImage.setObjectName(_fromUtf8("btnOpenImage"))
        self.horizontalLayout.addWidget(self.btnOpenImage)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton = QtGui.QToolButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/cancel")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.imagelabel = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagelabel.sizePolicy().hasHeightForWidth())
        self.imagelabel.setSizePolicy(sizePolicy)
        self.imagelabel.setStyleSheet(_fromUtf8(""))
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagelabel.setObjectName(_fromUtf8("imagelabel"))
        self.verticalLayout.addWidget(self.imagelabel)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(imageviewer)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("pressed()")), imageviewer.close)
        QtCore.QMetaObject.connectSlotsByName(imageviewer)

    def retranslateUi(self, imageviewer):
        imageviewer.setWindowTitle(QtGui.QApplication.translate("imageviewer", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOpenImage.setText(QtGui.QApplication.translate("imageviewer", "Open in External Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("imageviewer", "Tap image to close", None, QtGui.QApplication.UnicodeUTF8))
        self.imagelabel.setText(QtGui.QApplication.translate("imageviewer", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
