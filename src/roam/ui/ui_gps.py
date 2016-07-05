# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_gps.ui'
#
# Created: Thu Mar 12 14:47:56 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_gpsWidget(object):
    def setupUi(self, gpsWidget):
        gpsWidget.setObjectName(_fromUtf8("gpsWidget"))
        gpsWidget.resize(853, 736)
        gpsWidget.setAutoFillBackground(False)
        gpsWidget.setStyleSheet(_fromUtf8("QLabel[large=true] {\n"
"    color: #4f4f4f;\n"
"    font: 25pt \"Segoe UI\" ;\n"
"}\n"
"\n"
"QLabel[active=true] {\n"
"    color: rgb(0, 197, 95);\n"
"}\n"
"\n"
"QLabel[active=false] {\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"* {\n"
"      font: 20px \"Segoe UI\" ;\n"
"}    "))
        self.gridLayout_3 = QtGui.QGridLayout(gpsWidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.activeLabel = QtGui.QLabel(gpsWidget)
        self.activeLabel.setProperty(_fromUtf8("large"), True)
        self.activeLabel.setProperty(_fromUtf8("active"), False)
        self.activeLabel.setObjectName(_fromUtf8("activeLabel"))
        self.gridLayout_3.addWidget(self.activeLabel, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(gpsWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtGui.QLabel(gpsWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.latLabel = QtGui.QLabel(gpsWidget)
        self.latLabel.setText(_fromUtf8(""))
        self.latLabel.setObjectName(_fromUtf8("latLabel"))
        self.gridLayout.addWidget(self.latLabel, 1, 0, 1, 1)
        self.longLabel = QtGui.QLabel(gpsWidget)
        self.longLabel.setText(_fromUtf8(""))
        self.longLabel.setObjectName(_fromUtf8("longLabel"))
        self.gridLayout.addWidget(self.longLabel, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(gpsWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.yLabel = QtGui.QLabel(gpsWidget)
        self.yLabel.setText(_fromUtf8(""))
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.gridLayout_2.addWidget(self.yLabel, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(gpsWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.xLabel = QtGui.QLabel(gpsWidget)
        self.xLabel.setText(_fromUtf8(""))
        self.xLabel.setObjectName(_fromUtf8("xLabel"))
        self.gridLayout_2.addWidget(self.xLabel, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(gpsWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_8 = QtGui.QLabel(gpsWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_10 = QtGui.QLabel(gpsWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.pdopLabel = QtGui.QLabel(gpsWidget)
        self.pdopLabel.setText(_fromUtf8(""))
        self.pdopLabel.setObjectName(_fromUtf8("pdopLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pdopLabel)
        self.hdopLabel = QtGui.QLabel(gpsWidget)
        self.hdopLabel.setText(_fromUtf8(""))
        self.hdopLabel.setObjectName(_fromUtf8("hdopLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.hdopLabel)
        self.vdopLabel = QtGui.QLabel(gpsWidget)
        self.vdopLabel.setText(_fromUtf8(""))
        self.vdopLabel.setObjectName(_fromUtf8("vdopLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.vdopLabel)
        self.gridLayout_3.addLayout(self.formLayout, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 575, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 0, 1, 1)
        self.trackinglabel = QtGui.QLabel(gpsWidget)
        self.trackinglabel.setProperty(_fromUtf8("large"), True)
        self.trackinglabel.setProperty(_fromUtf8("active"), False)
        self.trackinglabel.setObjectName(_fromUtf8("trackinglabel"))
        self.gridLayout_3.addWidget(self.trackinglabel, 0, 1, 1, 1)
        self.logginginfolabel = QtGui.QLabel(gpsWidget)
        self.logginginfolabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.logginginfolabel.setWordWrap(True)
        self.logginginfolabel.setObjectName(_fromUtf8("logginginfolabel"))
        self.gridLayout_3.addWidget(self.logginginfolabel, 2, 1, 3, 1)

        self.retranslateUi(gpsWidget)
        QtCore.QMetaObject.connectSlotsByName(gpsWidget)

    def retranslateUi(self, gpsWidget):
        gpsWidget.setWindowTitle(QtGui.QApplication.translate("gpsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.activeLabel.setText(QtGui.QApplication.translate("gpsWidget", "GPS Not Active", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("gpsWidget", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("gpsWidget", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("gpsWidget", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("gpsWidget", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("gpsWidget", "HDOP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("gpsWidget", "VDOP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("gpsWidget", "PDOP", None, QtGui.QApplication.UnicodeUTF8))
        self.trackinglabel.setText(QtGui.QApplication.translate("gpsWidget", "GPS Logging Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.logginginfolabel.setText(QtGui.QApplication.translate("gpsWidget", "When GPS logging is active all GPS locations are logged into a set layer.", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
import resources_rc
import resources_rc
