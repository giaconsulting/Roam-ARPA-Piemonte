# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_helppage.ui'
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

class Ui_apphelpwidget(object):
    def setupUi(self, apphelpwidget):
        apphelpwidget.setObjectName(_fromUtf8("apphelpwidget"))
        apphelpwidget.resize(329, 559)
        apphelpwidget.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(apphelpwidget)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.helpframe = QtGui.QFrame(apphelpwidget)
        self.helpframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.helpframe.setFrameShadow(QtGui.QFrame.Raised)
        self.helpframe.setObjectName(_fromUtf8("helpframe"))
        self.gridLayout_2 = QtGui.QGridLayout(self.helpframe)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.webView = QtWebKit.QWebView(self.helpframe)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout_2.addWidget(self.webView, 1, 0, 1, 1)
        self.headerlabel = QtGui.QLabel(self.helpframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerlabel.sizePolicy().hasHeightForWidth())
        self.headerlabel.setSizePolicy(sizePolicy)
        self.headerlabel.setObjectName(_fromUtf8("headerlabel"))
        self.gridLayout_2.addWidget(self.headerlabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.helpframe, 0, 0, 1, 1)

        self.retranslateUi(apphelpwidget)
        QtCore.QMetaObject.connectSlotsByName(apphelpwidget)

    def retranslateUi(self, apphelpwidget):
        apphelpwidget.setWindowTitle(QtGui.QApplication.translate("apphelpwidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.headerlabel.setText(QtGui.QApplication.translate("apphelpwidget", "Help", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
