# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\project_installer\ui_project.ui'
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

class Ui_ProjectWidget(object):
    def setupUi(self, ProjectWidget):
        ProjectWidget.setObjectName(_fromUtf8("ProjectWidget"))
        ProjectWidget.resize(415, 397)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.projectlabel = QtGui.QLabel(ProjectWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.projectlabel.setFont(font)
        self.projectlabel.setObjectName(_fromUtf8("projectlabel"))
        self.verticalLayout.addWidget(self.projectlabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(ProjectWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(ProjectWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollarea = QtGui.QScrollArea(self.groupBox)
        self.scrollarea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setObjectName(_fromUtf8("scrollarea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 413, 288))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.scrollarea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollarea)
        self.verticalLayout.addWidget(self.groupBox)
        self.postinstalllabel = QtGui.QLabel(ProjectWidget)
        self.postinstalllabel.setOpenExternalLinks(False)
        self.postinstalllabel.setObjectName(_fromUtf8("postinstalllabel"))
        self.verticalLayout.addWidget(self.postinstalllabel)

        self.retranslateUi(ProjectWidget)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), ProjectWidget.save)
        QtCore.QObject.connect(self.postinstalllabel, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), ProjectWidget.runinstallscripts)
        QtCore.QMetaObject.connectSlotsByName(ProjectWidget)

    def retranslateUi(self, ProjectWidget):
        ProjectWidget.setWindowTitle(QtGui.QApplication.translate("ProjectWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.projectlabel.setText(QtGui.QApplication.translate("ProjectWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ProjectWidget", "Update Project", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ProjectWidget", "User values", None, QtGui.QApplication.UnicodeUTF8))
        self.postinstalllabel.setText(QtGui.QApplication.translate("ProjectWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff0004;\">Note: </span><span style=\" font-size:12pt; color:#000000;\">Post install scripts found in project folder.  </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">          Will be run on when project is updated or </span><a href=\"runnow\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Run Now</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

