# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_legend.ui'
#
# Created: Thu Mar 12 14:47:58 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_legendsWidget(object):
    def setupUi(self, legendsWidget):
        legendsWidget.setObjectName(_fromUtf8("legendsWidget"))
        legendsWidget.resize(715, 542)
        legendsWidget.setStyleSheet(_fromUtf8("QWidget{background-colorr: rgb(0, 0, 0,0);}\n"
"\n"
"QLabel#settingsLabel {\n"
"    color: #4f4f4f;\n"
"    font: 25pt \"Segoe UI\" ;\n"
"}\n"
"\n"
"    * {\n"
"            font: 12px \"Segoe UI\" ;\n"
"        }    "))
        self.gridLayout = QtGui.QGridLayout(legendsWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrolLegend = QtGui.QScrollArea(legendsWidget)
        self.scrolLegend.setAutoFillBackground(True)
        self.scrolLegend.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrolLegend.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrolLegend.setWidgetResizable(True)
        self.scrolLegend.setObjectName(_fromUtf8("scrolLegend"))
        self.legendList = QtGui.QWidget()
        self.legendList.setGeometry(QtCore.QRect(0, 0, 696, 523))
        self.legendList.setAutoFillBackground(True)
        self.legendList.setStyleSheet(_fromUtf8(""))
        self.legendList.setObjectName(_fromUtf8("legendList"))
        self.scrolLegend.setWidget(self.legendList)
        self.gridLayout.addWidget(self.scrolLegend, 0, 0, 1, 1)

        self.retranslateUi(legendsWidget)
        QtCore.QMetaObject.connectSlotsByName(legendsWidget)

    def retranslateUi(self, legendsWidget):
        legendsWidget.setWindowTitle(QtGui.QApplication.translate("legendsWidget", "Legend", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
import resources_rc
import resources_rc
