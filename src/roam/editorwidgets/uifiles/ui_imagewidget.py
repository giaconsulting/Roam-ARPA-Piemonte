# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\editorwidgets\uifiles\ui_imagewidget.ui'
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

class Ui_imagewidget(object):
    def setupUi(self, imagewidget):
        imagewidget.setObjectName(_fromUtf8("imagewidget"))
        imagewidget.resize(128, 121)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(imagewidget.sizePolicy().hasHeightForWidth())
        imagewidget.setSizePolicy(sizePolicy)
        imagewidget.setMaximumSize(QtCore.QSize(999999, 300))
        imagewidget.setMouseTracking(True)
        imagewidget.setStyleSheet(_fromUtf8("QPushButton \n"
"{\n"
" border: none;\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(imagewidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.image = QtGui.QLabel(imagewidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMaximumSize(QtCore.QSize(9999999, 999999))
        self.image.setText(_fromUtf8(""))
        self.image.setTextFormat(QtCore.Qt.RichText)
        self.image.setPixmap(QtGui.QPixmap(_fromUtf8(":/widgets/add")))
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setOpenExternalLinks(False)
        self.image.setObjectName(_fromUtf8("image"))
        self.gridLayout.addWidget(self.image, 1, 0, 1, 6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 5)
        self.deletebutton = QtGui.QPushButton(imagewidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deletebutton.sizePolicy().hasHeightForWidth())
        self.deletebutton.setSizePolicy(sizePolicy)
        self.deletebutton.setMaximumSize(QtCore.QSize(40, 40))
        self.deletebutton.setStyleSheet(_fromUtf8("border-color: none;"))
        self.deletebutton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/delete")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletebutton.setIcon(icon)
        self.deletebutton.setIconSize(QtCore.QSize(24, 24))
        self.deletebutton.setFlat(True)
        self.deletebutton.setObjectName(_fromUtf8("deletebutton"))
        self.gridLayout.addWidget(self.deletebutton, 0, 0, 1, 1)
        self.selectbutton = QtGui.QPushButton(imagewidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectbutton.sizePolicy().hasHeightForWidth())
        self.selectbutton.setSizePolicy(sizePolicy)
        self.selectbutton.setMaximumSize(QtCore.QSize(40, 40))
        self.selectbutton.setStyleSheet(_fromUtf8("border-color: none;"))
        self.selectbutton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/widgets/reload")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectbutton.setIcon(icon1)
        self.selectbutton.setIconSize(QtCore.QSize(24, 24))
        self.selectbutton.setFlat(True)
        self.selectbutton.setObjectName(_fromUtf8("selectbutton"))
        self.gridLayout.addWidget(self.selectbutton, 2, 0, 1, 1)
        self.editButton = QtGui.QPushButton(imagewidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editButton.sizePolicy().hasHeightForWidth())
        self.editButton.setSizePolicy(sizePolicy)
        self.editButton.setMaximumSize(QtCore.QSize(40, 40))
        self.editButton.setStyleSheet(_fromUtf8("border-color: none;"))
        self.editButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/widgets/blue")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setIconSize(QtCore.QSize(24, 24))
        self.editButton.setFlat(True)
        self.editButton.setObjectName(_fromUtf8("editButton"))
        self.gridLayout.addWidget(self.editButton, 2, 1, 1, 1)

        self.retranslateUi(imagewidget)
        QtCore.QMetaObject.connectSlotsByName(imagewidget)

    def retranslateUi(self, imagewidget):
        imagewidget.setWindowTitle(QtGui.QApplication.translate("imagewidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
import resources_rc
import resources_rc
