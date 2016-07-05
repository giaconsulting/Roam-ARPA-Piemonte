# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\editorwidgets\uifiles\ui_singlestepper.ui'
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

class Ui_stepper(object):
    def setupUi(self, stepper):
        stepper.setObjectName(_fromUtf8("stepper"))
        stepper.resize(919, 23)
        self.horizontalLayout = QtGui.QHBoxLayout(stepper)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stepDown = QtGui.QPushButton(stepper)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepDown.sizePolicy().hasHeightForWidth())
        self.stepDown.setSizePolicy(sizePolicy)
        self.stepDown.setStyleSheet(_fromUtf8(""))
        self.stepDown.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/previous")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stepDown.setIcon(icon)
        self.stepDown.setIconSize(QtCore.QSize(24, 24))
        self.stepDown.setObjectName(_fromUtf8("stepDown"))
        self.horizontalLayout.addWidget(self.stepDown)
        self.stepUp = QtGui.QPushButton(stepper)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepUp.sizePolicy().hasHeightForWidth())
        self.stepUp.setSizePolicy(sizePolicy)
        self.stepUp.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/next")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stepUp.setIcon(icon1)
        self.stepUp.setIconSize(QtCore.QSize(24, 24))
        self.stepUp.setObjectName(_fromUtf8("stepUp"))
        self.horizontalLayout.addWidget(self.stepUp)

        self.retranslateUi(stepper)
        QtCore.QMetaObject.connectSlotsByName(stepper)

    def retranslateUi(self, stepper):
        stepper.setWindowTitle(QtGui.QApplication.translate("stepper", "Form", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
