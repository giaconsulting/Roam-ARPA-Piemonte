# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\configmanager\editorwidgets\uifiles\ui_photowidget_config.ui'
#
# Created: Thu Mar 12 14:48:03 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.defaultLocationText = QtGui.QLineEdit(Form)
        self.defaultLocationText.setObjectName(_fromUtf8("defaultLocationText"))
        self.horizontalLayout.addWidget(self.defaultLocationText)
        self.locatioButton = QtGui.QPushButton(Form)
        self.locatioButton.setObjectName(_fromUtf8("locatioButton"))
        self.horizontalLayout.addWidget(self.locatioButton)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtGui.QLabel(Form)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.savetofileCheck = QtGui.QCheckBox(Form)
        self.savetofileCheck.setText(_fromUtf8(""))
        self.savetofileCheck.setChecked(True)
        self.savetofileCheck.setObjectName(_fromUtf8("savetofileCheck"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.savetofileCheck)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Default Location", None, QtGui.QApplication.UnicodeUTF8))
        self.locatioButton.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "You may also use environment variables in place of hard paths. e.g %USERPROFILE%Pictures may be used to access the users home pictures folder ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Save to file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Saving to file will save the file into the _images folder inside the project folder.  If this is unticked it will be saved as binary or base64 based on the field type ", None, QtGui.QApplication.UnicodeUTF8))

