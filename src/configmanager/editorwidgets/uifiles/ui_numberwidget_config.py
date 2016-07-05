# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\configmanager\editorwidgets\uifiles\ui_numberwidget_config.ui'
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
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.minEdit = QtGui.QLineEdit(Form)
        self.minEdit.setObjectName(_fromUtf8("minEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.minEdit)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.maxEdit = QtGui.QLineEdit(Form)
        self.maxEdit.setObjectName(_fromUtf8("maxEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.maxEdit)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        self.prefixEdit = QtGui.QLineEdit(Form)
        self.prefixEdit.setObjectName(_fromUtf8("prefixEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.prefixEdit)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.suffixEdit = QtGui.QLineEdit(Form)
        self.suffixEdit.setObjectName(_fromUtf8("suffixEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.suffixEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Minimum value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Maximum value", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Suffix", None, QtGui.QApplication.UnicodeUTF8))

