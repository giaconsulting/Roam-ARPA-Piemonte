# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\roam\ui\ui_datatimerpicker.ui'
#
# Created: Thu Mar 12 14:47:55 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_datatimerpicker(object):
    def setupUi(self, datatimerpicker):
        datatimerpicker.setObjectName(_fromUtf8("datatimerpicker"))
        datatimerpicker.resize(872, 624)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(datatimerpicker.sizePolicy().hasHeightForWidth())
        datatimerpicker.setSizePolicy(sizePolicy)
        datatimerpicker.setStyleSheet(_fromUtf8(""))
        self.gridLayout_2 = QtGui.QGridLayout(datatimerpicker)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(datatimerpicker)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setProperty(_fromUtf8("headerlabel"), True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.closebutton = QtGui.QToolButton(datatimerpicker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebutton.sizePolicy().hasHeightForWidth())
        self.closebutton.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/widgets/cancel")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setIconSize(QtCore.QSize(48, 48))
        self.closebutton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.closebutton.setAutoRaise(True)
        self.closebutton.setObjectName(_fromUtf8("closebutton"))
        self.horizontalLayout.addWidget(self.closebutton)
        self.okButton = QtGui.QToolButton(datatimerpicker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.okButton.setIcon(icon1)
        self.okButton.setIconSize(QtCore.QSize(48, 48))
        self.okButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.okButton.setAutoRaise(True)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.line = QtGui.QFrame(datatimerpicker)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.setasnowbutton = QtGui.QPushButton(datatimerpicker)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.setasnowbutton.setFont(font)
        self.setasnowbutton.setObjectName(_fromUtf8("setasnowbutton"))
        self.gridLayout_2.addWidget(self.setasnowbutton, 3, 0, 1, 2)
        self.datepicker = QtGui.QCalendarWidget(datatimerpicker)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datepicker.sizePolicy().hasHeightForWidth())
        self.datepicker.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.datepicker.setFont(font)
        self.datepicker.setObjectName(_fromUtf8("datepicker"))
        self.gridLayout_2.addWidget(self.datepicker, 4, 0, 1, 1)
        self.timesection = QtGui.QFrame(datatimerpicker)
        self.timesection.setObjectName(_fromUtf8("timesection"))
        self.gridLayout = QtGui.QGridLayout(self.timesection)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hourpicker = QtGui.QListWidget(self.timesection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourpicker.sizePolicy().hasHeightForWidth())
        self.hourpicker.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.hourpicker.setFont(font)
        self.hourpicker.setStyleSheet(_fromUtf8(""))
        self.hourpicker.setFrameShape(QtGui.QFrame.NoFrame)
        self.hourpicker.setObjectName(_fromUtf8("hourpicker"))
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        QtGui.QListWidgetItem(self.hourpicker)
        self.gridLayout.addWidget(self.hourpicker, 0, 1, 1, 1)
        self.minutepicker = QtGui.QListWidget(self.timesection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minutepicker.sizePolicy().hasHeightForWidth())
        self.minutepicker.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.minutepicker.setFont(font)
        self.minutepicker.setFrameShape(QtGui.QFrame.NoFrame)
        self.minutepicker.setObjectName(_fromUtf8("minutepicker"))
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        QtGui.QListWidgetItem(self.minutepicker)
        self.gridLayout.addWidget(self.minutepicker, 0, 3, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ambutton = QtGui.QPushButton(self.timesection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ambutton.sizePolicy().hasHeightForWidth())
        self.ambutton.setSizePolicy(sizePolicy)
        self.ambutton.setMinimumSize(QtCore.QSize(100, 100))
        self.ambutton.setCheckable(True)
        self.ambutton.setObjectName(_fromUtf8("ambutton"))
        self.verticalLayout.addWidget(self.ambutton)
        self.pmbutton = QtGui.QPushButton(self.timesection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pmbutton.sizePolicy().hasHeightForWidth())
        self.pmbutton.setSizePolicy(sizePolicy)
        self.pmbutton.setMinimumSize(QtCore.QSize(100, 100))
        self.pmbutton.setCheckable(True)
        self.pmbutton.setObjectName(_fromUtf8("pmbutton"))
        self.verticalLayout.addWidget(self.pmbutton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 4, 1, 1)
        self.line_2 = QtGui.QFrame(self.timesection)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 2, 1, 1)
        self.line_3 = QtGui.QFrame(self.timesection)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.timesection, 4, 1, 1, 1)
        self.label = QtGui.QLabel(datatimerpicker)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)

        self.retranslateUi(datatimerpicker)
        QtCore.QMetaObject.connectSlotsByName(datatimerpicker)

    def retranslateUi(self, datatimerpicker):
        datatimerpicker.setWindowTitle(QtGui.QApplication.translate("datatimerpicker", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("datatimerpicker", "Pick a date and time", None, QtGui.QApplication.UnicodeUTF8))
        self.closebutton.setText(QtGui.QApplication.translate("datatimerpicker", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("datatimerpicker", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.setasnowbutton.setText(QtGui.QApplication.translate("datatimerpicker", "Today", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.hourpicker.isSortingEnabled()
        self.hourpicker.setSortingEnabled(False)
        self.hourpicker.item(0).setText(QtGui.QApplication.translate("datatimerpicker", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(1).setText(QtGui.QApplication.translate("datatimerpicker", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(2).setText(QtGui.QApplication.translate("datatimerpicker", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(3).setText(QtGui.QApplication.translate("datatimerpicker", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(4).setText(QtGui.QApplication.translate("datatimerpicker", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(5).setText(QtGui.QApplication.translate("datatimerpicker", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(6).setText(QtGui.QApplication.translate("datatimerpicker", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(7).setText(QtGui.QApplication.translate("datatimerpicker", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(8).setText(QtGui.QApplication.translate("datatimerpicker", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(9).setText(QtGui.QApplication.translate("datatimerpicker", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(10).setText(QtGui.QApplication.translate("datatimerpicker", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.item(11).setText(QtGui.QApplication.translate("datatimerpicker", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.hourpicker.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.minutepicker.isSortingEnabled()
        self.minutepicker.setSortingEnabled(False)
        self.minutepicker.item(0).setText(QtGui.QApplication.translate("datatimerpicker", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(1).setText(QtGui.QApplication.translate("datatimerpicker", "05", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(2).setText(QtGui.QApplication.translate("datatimerpicker", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(3).setText(QtGui.QApplication.translate("datatimerpicker", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(4).setText(QtGui.QApplication.translate("datatimerpicker", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(5).setText(QtGui.QApplication.translate("datatimerpicker", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(6).setText(QtGui.QApplication.translate("datatimerpicker", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(7).setText(QtGui.QApplication.translate("datatimerpicker", "35", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(8).setText(QtGui.QApplication.translate("datatimerpicker", "40", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(9).setText(QtGui.QApplication.translate("datatimerpicker", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(10).setText(QtGui.QApplication.translate("datatimerpicker", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.item(11).setText(QtGui.QApplication.translate("datatimerpicker", "55", None, QtGui.QApplication.UnicodeUTF8))
        self.minutepicker.setSortingEnabled(__sortingEnabled)
        self.ambutton.setText(QtGui.QApplication.translate("datatimerpicker", "AM", None, QtGui.QApplication.UnicodeUTF8))
        self.pmbutton.setText(QtGui.QApplication.translate("datatimerpicker", "PM", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
