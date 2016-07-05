# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\sviluppo\Roam\src\configmanager\ui\ui_projectwidget.ui'
#
# Created: Thu Mar 12 14:48:04 2015
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
        Form.resize(781, 733)
        Form.setStyleSheet(_fromUtf8("      * \n"
"      {\n"
"            font: 14px \"Segoe UI\" ;\n"
"        }    \n"
"\n"
"        QStackedWidget {\n"
"             background-color: rgb(255, 255, 255);\n"
"        }\n"
"\n"
"        QWidget#Form  {\n"
"             background-color: rgb(255, 255, 255);\n"
"        }        \n"
"\n"
"        QToolButton { \n"
"            padding: 4px;\n"
"            color: #4f4f4f;\n"
"         }\n"
"\n"
"        QToolButton:hover { \n"
"            padding: 4px;\n"
"            background-color: rgb(211, 228, 255);\n"
"         }\n"
"        \n"
"        QToolBar, QStatusBar {\n"
"            font: 75 14pt \"Calibri\";\n"
"            background: white;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QStatusBar::item {\n"
"                    border: none;\n"
"        }\n"
"        \n"
"        QLabel {\n"
"            color: #4f4f4f;\n"
"        }\n"
"        \n"
"        QPushButton { \n"
"            border: 1px solid #e1e1e1;\n"
"             padding: 6px;\n"
"            color: #4f4f4f;\n"
"         }\n"
"        \n"
"        QPushButton:hover { \n"
"            border: 1px solid #e1e1e1;\n"
"             padding: 6px;\n"
"            background-color: rgb(211, 228, 255);\n"
"         }\n"
"        \n"
"        QCheckBox {\n"
"            color: #4f4f4f;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down {\n"
"            width: 30px;\n"
"        }\n"
"        \n"
"        QComboBox {\n"
"            border: 1px solid #d3d3d3;\n"
"        }\n"
"\n"
"QLabel[isheader=true]\n"
"{\n"
"    font: 75 14pt \"Segoe UI\";\n"
"}\n"
"\n"
"QLabel[warning=true]\n"
"{\n"
"    color: rgb(255, 67, 30);\n"
"}\n"
"    "))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.project_info_page = QtGui.QWidget()
        self.project_info_page.setObjectName(_fromUtf8("project_info_page"))
        self.gridLayout_11 = QtGui.QGridLayout(self.project_info_page)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.titleText = QtGui.QLineEdit(self.project_info_page)
        self.titleText.setObjectName(_fromUtf8("titleText"))
        self.gridLayout_11.addWidget(self.titleText, 1, 0, 1, 2)
        self.descriptionText = QtGui.QPlainTextEdit(self.project_info_page)
        self.descriptionText.setObjectName(_fromUtf8("descriptionText"))
        self.gridLayout_11.addWidget(self.descriptionText, 3, 0, 1, 2)
        self.selectLayers = QtGui.QListView(self.project_info_page)
        self.selectLayers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.selectLayers.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.selectLayers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.selectLayers.setObjectName(_fromUtf8("selectLayers"))
        self.gridLayout_11.addWidget(self.selectLayers, 5, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.versionText = QtGui.QLineEdit(self.project_info_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionText.sizePolicy().hasHeightForWidth())
        self.versionText.setSizePolicy(sizePolicy)
        self.versionText.setObjectName(_fromUtf8("versionText"))
        self.horizontalLayout_3.addWidget(self.versionText)
        self.roamVersionLabel = QtGui.QLabel(self.project_info_page)
        self.roamVersionLabel.setObjectName(_fromUtf8("roamVersionLabel"))
        self.horizontalLayout_3.addWidget(self.roamVersionLabel)
        self.gridLayout_11.addLayout(self.horizontalLayout_3, 7, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.splashlabel = QtGui.QLabel(self.project_info_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splashlabel.sizePolicy().hasHeightForWidth())
        self.splashlabel.setSizePolicy(sizePolicy)
        self.splashlabel.setMinimumSize(QtCore.QSize(0, 300))
        self.splashlabel.setMaximumSize(QtCore.QSize(16777215, 300))
        self.splashlabel.setText(_fromUtf8(""))
        self.splashlabel.setScaledContents(True)
        self.splashlabel.setObjectName(_fromUtf8("splashlabel"))
        self.horizontalLayout_6.addWidget(self.splashlabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout_11.addLayout(self.horizontalLayout_6, 9, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.project_info_page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.project_info_page)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_11.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.project_info_page)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_11.addWidget(self.label_14, 8, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.project_info_page)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_11.addWidget(self.label_9, 6, 0, 1, 1)
        self.selectLayersLabel = QtGui.QLabel(self.project_info_page)
        self.selectLayersLabel.setObjectName(_fromUtf8("selectLayersLabel"))
        self.gridLayout_11.addWidget(self.selectLayersLabel, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.project_info_page)
        self.form_config_page = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_config_page.sizePolicy().hasHeightForWidth())
        self.form_config_page.setSizePolicy(sizePolicy)
        self.form_config_page.setObjectName(_fromUtf8("form_config_page"))
        self.gridLayout_3 = QtGui.QGridLayout(self.form_config_page)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.form_config_page)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.formLabelText = QtGui.QLineEdit(self.form_config_page)
        self.formLabelText.setObjectName(_fromUtf8("formLabelText"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.formLabelText)
        self.label_7 = QtGui.QLabel(self.form_config_page)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.layerCombo = QtGui.QComboBox(self.form_config_page)
        self.layerCombo.setEditable(False)
        self.layerCombo.setObjectName(_fromUtf8("layerCombo"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.layerCombo)
        self.label_5 = QtGui.QLabel(self.form_config_page)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formtypeCombo = QtGui.QComboBox(self.form_config_page)
        self.formtypeCombo.setObjectName(_fromUtf8("formtypeCombo"))
        self.formtypeCombo.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.formtypeCombo)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_16 = QtGui.QLabel(self.form_config_page)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_16)
        self.formfolderLabel = QtGui.QLabel(self.form_config_page)
        self.formfolderLabel.setText(_fromUtf8(""))
        self.formfolderLabel.setObjectName(_fromUtf8("formfolderLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.formfolderLabel)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formtab = QtGui.QTabWidget(self.form_config_page)
        self.formtab.setTabShape(QtGui.QTabWidget.Rounded)
        self.formtab.setIconSize(QtCore.QSize(24, 24))
        self.formtab.setObjectName(_fromUtf8("formtab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab)
        self.gridLayout_10.setContentsMargins(3, 3, 3, 0)
        self.gridLayout_10.setHorizontalSpacing(12)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.formframe = QtGui.QFrame(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formframe.sizePolicy().hasHeightForWidth())
        self.formframe.setSizePolicy(sizePolicy)
        self.formframe.setFrameShape(QtGui.QFrame.NoFrame)
        self.formframe.setFrameShadow(QtGui.QFrame.Raised)
        self.formframe.setObjectName(_fromUtf8("formframe"))
        self.gridLayout_6 = QtGui.QGridLayout(self.formframe)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setHorizontalSpacing(12)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.frame = QtGui.QFrame(self.formframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addWidgetButton = QtGui.QToolButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/add")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addWidgetButton.setIcon(icon)
        self.addWidgetButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.addWidgetButton.setAutoRaise(True)
        self.addWidgetButton.setObjectName(_fromUtf8("addWidgetButton"))
        self.horizontalLayout_2.addWidget(self.addWidgetButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.removeWidgetButton = QtGui.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/remove")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeWidgetButton.setIcon(icon1)
        self.removeWidgetButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.removeWidgetButton.setAutoRaise(True)
        self.removeWidgetButton.setObjectName(_fromUtf8("removeWidgetButton"))
        self.horizontalLayout_2.addWidget(self.removeWidgetButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widgetlist = QtGui.QTreeView(self.frame)
        self.widgetlist.setFrameShape(QtGui.QFrame.NoFrame)
        self.widgetlist.setDragEnabled(True)
        self.widgetlist.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.widgetlist.setAlternatingRowColors(True)
        self.widgetlist.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.widgetlist.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.widgetlist.setIconSize(QtCore.QSize(24, 24))
        self.widgetlist.setAnimated(True)
        self.widgetlist.setObjectName(_fromUtf8("widgetlist"))
        self.widgetlist.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.widgetlist)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 3, 0, 1, 2)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.formframe)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_13.setMargin(0)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.widgetframe = QtGui.QFrame(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetframe.sizePolicy().hasHeightForWidth())
        self.widgetframe.setSizePolicy(sizePolicy)
        self.widgetframe.setObjectName(_fromUtf8("widgetframe"))
        self.formLayout_3 = QtGui.QFormLayout(self.widgetframe)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setContentsMargins(3, 3, 3, 0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_4 = QtGui.QLabel(self.widgetframe)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.fieldList = QtGui.QComboBox(self.widgetframe)
        self.fieldList.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldList.sizePolicy().hasHeightForWidth())
        self.fieldList.setSizePolicy(sizePolicy)
        self.fieldList.setEditable(False)
        self.fieldList.setObjectName(_fromUtf8("fieldList"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.fieldList)
        self.fieldwarninglabel = QtGui.QLabel(self.widgetframe)
        self.fieldwarninglabel.setWordWrap(True)
        self.fieldwarninglabel.setProperty(_fromUtf8("warning"), True)
        self.fieldwarninglabel.setObjectName(_fromUtf8("fieldwarninglabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.fieldwarninglabel)
        self.label_11 = QtGui.QLabel(self.widgetframe)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.nameText = QtGui.QLineEdit(self.widgetframe)
        self.nameText.setObjectName(_fromUtf8("nameText"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.nameText)
        self.label_8 = QtGui.QLabel(self.widgetframe)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.widgetCombo = QtGui.QComboBox(self.widgetframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetCombo.sizePolicy().hasHeightForWidth())
        self.widgetCombo.setSizePolicy(sizePolicy)
        self.widgetCombo.setObjectName(_fromUtf8("widgetCombo"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.widgetCombo)
        self.label_10 = QtGui.QLabel(self.widgetframe)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_10)
        self.requiredCheck = QtGui.QCheckBox(self.widgetframe)
        self.requiredCheck.setText(_fromUtf8(""))
        self.requiredCheck.setObjectName(_fromUtf8("requiredCheck"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.requiredCheck)
        self.label_12 = QtGui.QLabel(self.widgetframe)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_12)
        self.hiddenCheck = QtGui.QCheckBox(self.widgetframe)
        self.hiddenCheck.setText(_fromUtf8(""))
        self.hiddenCheck.setObjectName(_fromUtf8("hiddenCheck"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.hiddenCheck)
        self.label_13 = QtGui.QLabel(self.widgetframe)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_13)
        self.readonlyCombo = QtGui.QComboBox(self.widgetframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readonlyCombo.sizePolicy().hasHeightForWidth())
        self.readonlyCombo.setSizePolicy(sizePolicy)
        self.readonlyCombo.setObjectName(_fromUtf8("readonlyCombo"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.readonlyCombo)
        self.label = QtGui.QLabel(self.widgetframe)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.defaultvalueText = QtGui.QLineEdit(self.widgetframe)
        self.defaultvalueText.setObjectName(_fromUtf8("defaultvalueText"))
        self.horizontalLayout_7.addWidget(self.defaultvalueText)
        self.expressionButton = QtGui.QPushButton(self.widgetframe)
        self.expressionButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Expression")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expressionButton.setIcon(icon2)
        self.expressionButton.setIconSize(QtCore.QSize(24, 24))
        self.expressionButton.setObjectName(_fromUtf8("expressionButton"))
        self.horizontalLayout_7.addWidget(self.expressionButton)
        self.formLayout_3.setLayout(9, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.widgetFrame_2 = QtGui.QFrame(self.widgetframe)
        self.widgetFrame_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrame_2.sizePolicy().hasHeightForWidth())
        self.widgetFrame_2.setSizePolicy(sizePolicy)
        self.widgetFrame_2.setMinimumSize(QtCore.QSize(350, 0))
        self.widgetFrame_2.setBaseSize(QtCore.QSize(200, 0))
        self.widgetFrame_2.setObjectName(_fromUtf8("widgetFrame_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widgetFrame_2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widgetstack = QtGui.QStackedWidget(self.widgetFrame_2)
        self.widgetstack.setStyleSheet(_fromUtf8(""))
        self.widgetstack.setObjectName(_fromUtf8("widgetstack"))
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.widgetstack.addWidget(self.page_4)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.widgetstack.addWidget(self.page_5)
        self.verticalLayout_5.addWidget(self.widgetstack)
        self.formLayout_3.setWidget(12, QtGui.QFormLayout.SpanningRole, self.widgetFrame_2)
        self.gridLayout_13.addWidget(self.widgetframe, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.formLayout = QtGui.QFormLayout(self.tab_4)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_15 = QtGui.QLabel(self.tab_4)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.savevalueCheck = QtGui.QCheckBox(self.tab_4)
        self.savevalueCheck.setText(_fromUtf8(""))
        self.savevalueCheck.setObjectName(_fromUtf8("savevalueCheck"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.savevalueCheck)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_10.addWidget(self.formframe, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 0, 1, 1, 1)
        self.formtab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_9.setMargin(0)
        self.gridLayout_9.setHorizontalSpacing(8)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.frame_4 = QtGui.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.scrollArea = QtGui.QScrollArea(self.frame_4)
        self.scrollArea.setStyleSheet(_fromUtf8(""))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.frame_2 = QtGui.QWidget()
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 777, 491))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_12 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_12.setMargin(0)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.scrollArea.setWidget(self.frame_2)
        self.gridLayout_7.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_4, 1, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setProperty(_fromUtf8("warning"), True)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_9.addWidget(self.label_21, 0, 0, 1, 1)
        self.formtab.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.formtab, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.form_config_page)
        self.map_page = QtGui.QWidget()
        self.map_page.setObjectName(_fromUtf8("map_page"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.map_page)
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.canvas = QgsMapCanvas(self.map_page)
        self.canvas.setStyleSheet(_fromUtf8(""))
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.verticalLayout_3.addWidget(self.canvas)
        self.stackedWidget.addWidget(self.map_page)
        self.blank = QtGui.QWidget()
        self.blank.setObjectName(_fromUtf8("blank"))
        self.gridLayout_8 = QtGui.QGridLayout(self.blank)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.stackedWidget.addWidget(self.blank)
        self.roam_page = QtGui.QWidget()
        self.roam_page.setObjectName(_fromUtf8("roam_page"))
        self.gridLayout_2 = QtGui.QGridLayout(self.roam_page)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_42 = QtGui.QLabel(self.roam_page)
        self.label_42.setWordWrap(True)
        self.label_42.setProperty(_fromUtf8("isheader"), True)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_2.addWidget(self.label_42, 0, 0, 1, 3)
        self.groupBox_3 = QtGui.QGroupBox(self.roam_page)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.versionLabel1 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionLabel1.sizePolicy().hasHeightForWidth())
        self.versionLabel1.setSizePolicy(sizePolicy)
        self.versionLabel1.setScaledContents(False)
        self.versionLabel1.setObjectName(_fromUtf8("versionLabel1"))
        self.horizontalLayout_9.addWidget(self.versionLabel1)
        self.versionLabel = QtGui.QLabel(self.groupBox_3)
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.horizontalLayout_9.addWidget(self.versionLabel)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_8.addWidget(self.label_19)
        self.qgisapiLabel = QtGui.QLabel(self.groupBox_3)
        self.qgisapiLabel.setObjectName(_fromUtf8("qgisapiLabel"))
        self.horizontalLayout_8.addWidget(self.qgisapiLabel)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 1, 0, 1, 2)
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMaximumSize(QtCore.QSize(270, 250))
        self.label_17.setText(_fromUtf8(""))
        self.label_17.setPixmap(QtGui.QPixmap(_fromUtf8(":/branding/dms")))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_5.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setMaximumSize(QtCore.QSize(150, 150))
        self.label_20.setText(_fromUtf8(""))
        self.label_20.setPixmap(QtGui.QPixmap(_fromUtf8(":/branding/qgis")))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_5.addWidget(self.label_20, 3, 1, 1, 1)
        self.label_41 = QtGui.QLabel(self.groupBox_3)
        self.label_41.setOpenExternalLinks(True)
        self.label_41.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_5.addWidget(self.label_41, 5, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_3)
        self.label_18.setOpenExternalLinks(True)
        self.label_18.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_5.addWidget(self.label_18, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 3, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 3)
        self.label_43 = QtGui.QLabel(self.roam_page)
        self.label_43.setWordWrap(True)
        self.label_43.setProperty(_fromUtf8("isheader"), True)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_2.addWidget(self.label_43, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.roam_page)
        self.forms_page = QtGui.QWidget()
        self.forms_page.setObjectName(_fromUtf8("forms_page"))
        self.formLayout_5 = QtGui.QFormLayout(self.forms_page)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.selectLayers_2 = QtGui.QListView(self.forms_page)
        self.selectLayers_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.selectLayers_2.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.selectLayers_2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.selectLayers_2.setObjectName(_fromUtf8("selectLayers_2"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.selectLayers_2)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.formLayout_5.setItem(3, QtGui.QFormLayout.FieldRole, spacerItem6)
        self.formslayerlabel = QtGui.QLabel(self.forms_page)
        self.formslayerlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.formslayerlabel.setWordWrap(True)
        self.formslayerlabel.setProperty(_fromUtf8("isheader"), True)
        self.formslayerlabel.setObjectName(_fromUtf8("formslayerlabel"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.SpanningRole, self.formslayerlabel)
        self.selectLayersLabel_2 = QtGui.QLabel(self.forms_page)
        self.selectLayersLabel_2.setObjectName(_fromUtf8("selectLayersLabel_2"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.selectLayersLabel_2)
        self.stackedWidget.addWidget(self.forms_page)
        self.projects_page = ProjectsNode()
        self.projects_page.setObjectName(_fromUtf8("projects_page"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.projects_page)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.stackedWidget.addWidget(self.projects_page)
        self.invalidproject_page = QtGui.QWidget()
        self.invalidproject_page.setObjectName(_fromUtf8("invalidproject_page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.invalidproject_page)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formslayerlabel_2 = QtGui.QLabel(self.invalidproject_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formslayerlabel_2.sizePolicy().hasHeightForWidth())
        self.formslayerlabel_2.setSizePolicy(sizePolicy)
        self.formslayerlabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.formslayerlabel_2.setWordWrap(True)
        self.formslayerlabel_2.setProperty(_fromUtf8("isheader"), True)
        self.formslayerlabel_2.setObjectName(_fromUtf8("formslayerlabel_2"))
        self.verticalLayout.addWidget(self.formslayerlabel_2)
        self.reasons_label = QtGui.QLabel(self.invalidproject_page)
        self.reasons_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.reasons_label.setWordWrap(True)
        self.reasons_label.setProperty(_fromUtf8("isheader"), True)
        self.reasons_label.setObjectName(_fromUtf8("reasons_label"))
        self.verticalLayout.addWidget(self.reasons_label)
        self.stackedWidget.addWidget(self.invalidproject_page)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.projectlabel = QtGui.QLabel(Form)
        self.projectlabel.setProperty(_fromUtf8("isheader"), True)
        self.projectlabel.setObjectName(_fromUtf8("projectlabel"))
        self.horizontalLayout_4.addWidget(self.projectlabel)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.projectupdatedlabel = QtGui.QLabel(Form)
        self.projectupdatedlabel.setObjectName(_fromUtf8("projectupdatedlabel"))
        self.horizontalLayout_4.addWidget(self.projectupdatedlabel)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.projectbuttonframe = QtGui.QFrame(Form)
        self.projectbuttonframe.setFrameShape(QtGui.QFrame.NoFrame)
        self.projectbuttonframe.setFrameShadow(QtGui.QFrame.Raised)
        self.projectbuttonframe.setObjectName(_fromUtf8("projectbuttonframe"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.projectbuttonframe)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.openProjectFolderButton = QtGui.QToolButton(self.projectbuttonframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openProjectFolderButton.sizePolicy().hasHeightForWidth())
        self.openProjectFolderButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/folder")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openProjectFolderButton.setIcon(icon3)
        self.openProjectFolderButton.setIconSize(QtCore.QSize(24, 24))
        self.openProjectFolderButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.openProjectFolderButton.setAutoRaise(True)
        self.openProjectFolderButton.setObjectName(_fromUtf8("openProjectFolderButton"))
        self.horizontalLayout_5.addWidget(self.openProjectFolderButton)
        self.openinQGISButton = QtGui.QToolButton(self.projectbuttonframe)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openinQGISButton.sizePolicy().hasHeightForWidth())
        self.openinQGISButton.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/branding/qgis")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openinQGISButton.setIcon(icon4)
        self.openinQGISButton.setIconSize(QtCore.QSize(24, 24))
        self.openinQGISButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.openinQGISButton.setAutoRaise(True)
        self.openinQGISButton.setObjectName(_fromUtf8("openinQGISButton"))
        self.horizontalLayout_5.addWidget(self.openinQGISButton)
        self.toolButton_6 = QtGui.QToolButton(self.projectbuttonframe)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/save")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(24, 24))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.horizontalLayout_5.addWidget(self.toolButton_6)
        self.horizontalLayout_4.addWidget(self.projectbuttonframe)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.formtab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.toolButton_6, QtCore.SIGNAL(_fromUtf8("pressed()")), Form._saveproject)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.versionText.setInputMask(QtGui.QApplication.translate("Form", "0.0.0; ", None, QtGui.QApplication.UnicodeUTF8))
        self.roamVersionLabel.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Project Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "Splash", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Compatible Roam Version", None, QtGui.QApplication.UnicodeUTF8))
        self.selectLayersLabel.setText(QtGui.QApplication.translate("Form", "Enable any layers that should be enabled for selection. Selection layers can be used for data entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Capture Layer</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The layer that will contain the information from the form.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Note: </span><span style=\" font-style:italic;\">Only Select layers will show up here.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Capture Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.formtypeCombo.setItemText(0, QtGui.QApplication.translate("Form", "auto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "Form folder", None, QtGui.QApplication.UnicodeUTF8))
        self.addWidgetButton.setText(QtGui.QApplication.translate("Form", "Add Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.removeWidgetButton.setText(QtGui.QApplication.translate("Form", "Remove Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Field", None, QtGui.QApplication.UnicodeUTF8))
        self.fieldwarninglabel.setText(QtGui.QApplication.translate("Form", "Warning: Field is already used. Roam only supports one field per attribute. This attribute will be ignored when setting values.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Required</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This field must be completed before the form can be accpected.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setWhatsThis(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Required</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This field must be completed before the form can be accpected.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Required?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Hidden</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Is this field hidden when the form is open in Roam.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setWhatsThis(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Hidden</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Is this field hidden when the form is open in Roam.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "Hidden?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setWhatsThis(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Hidden</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Is this field hidden when the form is open in Roam.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Read Only", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Default Value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "Save last value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.formtab.setTabText(self.formtab.indexOf(self.tab), QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Form", "Default values not loaded in preview mode.", None, QtGui.QApplication.UnicodeUTF8))
        self.formtab.setTabText(self.formtab.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Form", "IntraMaps Roam Config Manager allows the creation and managment of Roam projects and forms.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel1.setText(QtGui.QApplication.translate("Form", "You are running Roam version:", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "that\'s running on QGIS API:", None, QtGui.QApplication.UnicodeUTF8))
        self.qgisapiLabel.setText(QtGui.QApplication.translate("Form", "{API}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/DMS-Aus/Roam\"><span style=\" text-decoration: underline; color:#0000ff;\">Project Home Page</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/DMS-Aus/Roam/issues?state=open\"><span style=\" text-decoration: underline; color:#0000ff;\">Issue Tracker</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/DMS-Aus/Roam/wiki\"><span style=\" text-decoration: underline; color:#0000ff;\">Project Wiki</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Created By </span><a href=\"mapsolutions.com.au\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; text-decoration: underline; color:#0000ff;\">DMS Australia</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">© 2013 Digital Mapping Solutions</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("Form", "Select the Project tree item on the left to create a new project", None, QtGui.QApplication.UnicodeUTF8))
        self.formslayerlabel.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400;\">Seems like this project doesn\'t have any select layers yet.  We need some point select layers in order to create data entry forms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"open-qgis\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; text-decoration: underline; color:#0000ff;\">Open QGIS </span></a><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400;\">to add layers to your QGIS project, then enable them for selection above.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.selectLayersLabel_2.setText(QtGui.QApplication.translate("Form", "Enable any layers that should be enabled for selection.  Selection layers can also be used for data capture.", None, QtGui.QApplication.UnicodeUTF8))
        self.formslayerlabel_2.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff5500;\">Oh no! Seems this project is invalid so we can\'t load it.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.reasons_label.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.projectlabel.setText(QtGui.QApplication.translate("Form", "{Project}", None, QtGui.QApplication.UnicodeUTF8))
        self.projectupdatedlabel.setText(QtGui.QApplication.translate("Form", "{project update label}", None, QtGui.QApplication.UnicodeUTF8))
        self.openProjectFolderButton.setText(QtGui.QApplication.translate("Form", "Open Project Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.openinQGISButton.setText(QtGui.QApplication.translate("Form", "Open In QGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_6.setText(QtGui.QApplication.translate("Form", "Save Project", None, QtGui.QApplication.UnicodeUTF8))

from qgis.gui import QgsMapCanvas
from configmanager.gui import ProjectsNode
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
import resources_rc
