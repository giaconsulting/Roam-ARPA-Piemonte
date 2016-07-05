# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_settings.ui'
#
# Created: Thu Mar 12 14:48:00 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settingsWidget(object):
    def setupUi(self, settingsWidget):
        settingsWidget.setObjectName(_fromUtf8("settingsWidget"))
        settingsWidget.resize(848, 786)
        settingsWidget.setAutoFillBackground(False)
        settingsWidget.setStyleSheet(_fromUtf8("QLabel#settingsLabel {\n"
"    color: #4f4f4f;\n"
"    font: 25pt \"Segoe UI\" ;\n"
"}\n"
"\n"
"    * {\n"
"            font: 20px \"Segoe UI\" ;\n"
"        }    "))
        self.gridLayout = QtGui.QGridLayout(settingsWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(settingsWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(-1)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.fullScreenCheck = QtGui.QCheckBox(self.groupBox)
        self.fullScreenCheck.setObjectName(_fromUtf8("fullScreenCheck"))
        self.gridLayout_2.addWidget(self.fullScreenCheck, 0, 0, 1, 1)
        self.keyboardCheck = QtGui.QCheckBox(self.groupBox)
        self.keyboardCheck.setChecked(True)
        self.keyboardCheck.setObjectName(_fromUtf8("keyboardCheck"))
        self.gridLayout_2.addWidget(self.keyboardCheck, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(settingsWidget)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gpsPortCombo = QtGui.QComboBox(self.groupBox_2)
        self.gpsPortCombo.setObjectName(_fromUtf8("gpsPortCombo"))
        self.horizontalLayout_2.addWidget(self.gpsPortCombo)
        self.refreshPortsButton = QtGui.QPushButton(self.groupBox_2)
        self.refreshPortsButton.setObjectName(_fromUtf8("refreshPortsButton"))
        self.horizontalLayout_2.addWidget(self.refreshPortsButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gpslocationCheck = QtGui.QCheckBox(self.groupBox_2)
        self.gpslocationCheck.setChecked(True)
        self.gpslocationCheck.setObjectName(_fromUtf8("gpslocationCheck"))
        self.gridLayout_3.addWidget(self.gpslocationCheck, 1, 1, 1, 1)
        self.gpscentermapCheck = QtGui.QCheckBox(self.groupBox_2)
        self.gpscentermapCheck.setChecked(True)
        self.gpscentermapCheck.setObjectName(_fromUtf8("gpscentermapCheck"))
        self.gridLayout_3.addWidget(self.gpscentermapCheck, 2, 1, 1, 1)
        self.gpsloggingCheck = QtGui.QCheckBox(self.groupBox_2)
        self.gpsloggingCheck.setChecked(True)
        self.gpsloggingCheck.setObjectName(_fromUtf8("gpsloggingCheck"))
        self.gridLayout_3.addWidget(self.gpsloggingCheck, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(settingsWidget)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(270, 250))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/branding/dms")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.qgisapiLabel = QtGui.QLabel(self.groupBox_3)
        self.qgisapiLabel.setObjectName(_fromUtf8("qgisapiLabel"))
        self.horizontalLayout_3.addWidget(self.qgisapiLabel)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.versionLabel1 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLabel1.sizePolicy().hasHeightForWidth())
        self.versionLabel1.setSizePolicy(sizePolicy)
        self.versionLabel1.setScaledContents(False)
        self.versionLabel1.setObjectName(_fromUtf8("versionLabel1"))
        self.horizontalLayout.addWidget(self.versionLabel1)
        self.versionLabel = QtGui.QLabel(self.groupBox_3)
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.horizontalLayout.addWidget(self.versionLabel)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 150))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/branding/qgis")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 4, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)

        self.retranslateUi(settingsWidget)
        QtCore.QMetaObject.connectSlotsByName(settingsWidget)

    def retranslateUi(self, settingsWidget):
        settingsWidget.setWindowTitle(QtGui.QApplication.translate("settingsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("settingsWidget", "Application", None, QtGui.QApplication.UnicodeUTF8))
        self.fullScreenCheck.setText(QtGui.QApplication.translate("settingsWidget", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.keyboardCheck.setText(QtGui.QApplication.translate("settingsWidget", "Use popout keyboard", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("settingsWidget", "GPS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("settingsWidget", "Connect via", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPortsButton.setText(QtGui.QApplication.translate("settingsWidget", "Refresh List", None, QtGui.QApplication.UnicodeUTF8))
        self.gpslocationCheck.setText(QtGui.QApplication.translate("settingsWidget", "Zoom to my location when GPS enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.gpscentermapCheck.setText(QtGui.QApplication.translate("settingsWidget", "Force map to follow GPS location", None, QtGui.QApplication.UnicodeUTF8))
        self.gpsloggingCheck.setText(QtGui.QApplication.translate("settingsWidget", "Enable GPS Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("settingsWidget", "GPS logging must be enable at the project level by an admin", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("settingsWidget", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("settingsWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Created By </span><a href=\"mapsolutions.com.au\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#0000ff;\">DMS Australia</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">© 2013 Digital Mapping Solutions</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("settingsWidget", "that\'s running on QGIS API:", None, QtGui.QApplication.UnicodeUTF8))
        self.qgisapiLabel.setText(QtGui.QApplication.translate("settingsWidget", "{API}", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel1.setText(QtGui.QApplication.translate("settingsWidget", "You are running Roam version:", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("settingsWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
import resources_rc
import resources_rc
