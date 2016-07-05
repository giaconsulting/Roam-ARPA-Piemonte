import os
from string import Template
from collections import OrderedDict
from PyQt4.QtGui import ( QWidget, QIcon, QListWidgetItem, QMouseEvent, QApplication, QButtonGroup, QColor, QColorDialog,
                         QCloseEvent, QComboBox, QSlider, QScrollArea, QRadioButton, QPixmap, QMouseEvent, QLabel, QPushButton, QMessageBox)
from PyQt4.QtCore import (Qt, QUrl,QEvent, pyqtSignal, QFile, QObject, QPoint, QRectF, QRect, QSize)
from PyQt4.QtWebKit import QWebPage
from qgis.core import (QgsExpression, QgsFeature, QgsMapLayer, QgsFeatureRequest)

from roam import utils
from roam.flickwidget import FlickCharm
from roam.htmlviewer import updateTemplate, clear_image_cache
from roam.ui.uifiles import (annotationdock_widget)
from roam.api import RoamEvents
from roam.dataaccess import database
from roam.api.utils import layer_by_name, values_from_feature
from PyQt4 import QtGui
from qgis.core import *
from qgis.gui import *


import templates

class AnnotationDock(annotationdock_widget, QWidget):

    def __init__(self, parent):
        super(AnnotationDock, self).__init__(parent)
        self.setupUi(self)
        self.PrincipalTools = [self.PointButton,self.paintButton,self.lineButton,self.polyButton,self.rectangleButton,self.circleButton]
        self.PoinToshow=[self.scrollAreaMarker,self.checkFillTransparency,self.checkLineTransparency,self.color,self.outlineSize]
        self.LineToshow=[self.Textinput,self.Transparency, self.StyleLine,self.Size,self.LineColor]
        self.showList = [self.radioList,self.radioNew,self.StyleList]
        self.drawTools = [self.endButton, self.refreshButton, self.undoButton, self.redoButton]
        self.OrizLine = [self.line_2,self.line_3]
        self.alldynacmic = [self.scrollAreaMarker,self.checkFillTransparency,self.checkLineTransparency,self.color,self.outlineSize,self.Textinput,self.Transparency, self.StyleLine,self.Size,self.LineColor,self.endButton, self.refreshButton, self.undoButton, self.redoButton,self.line_2,self.line_3]
        self.PointButton.clicked.connect(self.selectPoint)
        self.paintButton.clicked.connect(self.selectPaint)
        self.lineButton.clicked.connect(self.selectLine)
        self.polyButton.clicked.connect(self.selectPoly)
        self.rectangleButton.clicked.connect(self.selectRectangle)
        self.circleButton.clicked.connect(self.selectCircle)
        self.closeBarButton.clicked.connect(self.chiudi)
        self.arrowhead.clicked.connect(self.selectMarker)
        self.pentagon.clicked.connect(self.selectMarker)
        self.arrow.clicked.connect(self.selectMarker)
        self.filled_arrowhead.clicked.connect(self.selectMarker)
        self.triangle.clicked.connect(self.selectMarker)
        self.cross.clicked.connect(self.selectMarker)
        self.rectangle.clicked.connect(self.selectMarker)
        self.diamond.clicked.connect(self.selectMarker)
        self.circle.clicked.connect(self.selectMarker)
        self.regular_star.clicked.connect(self.selectMarker)
        self.endButton.pressed.connect(self.endEdit)
        self.refreshButton.pressed.connect(self.callRefresh)
        self.undoButton.clicked.connect(self.clickUndo)
        self.redoButton.clicked.connect(self.clickRedo)
        self.layerid=["point20150114085613922","line20150114085613640","polygon20150114085614076"]
        RoamEvents.unlockEndEdit.connect(self.unlockEndButton)
        RoamEvents.lockEndEdit.connect(self.lockEndButton)
        RoamEvents.closeAnnotation.connect(self.chiudi)
        RoamEvents.unlockUndoRedo.connect(self.UnlockUR)
        RoamEvents.lockUndoRedo.connect(self.LockUR)
        RoamEvents.unlockCancel.connect(self.unlockCancelButton)
        RoamEvents.addList.connect(self.addList)
        RoamEvents.lockCancel.connect(self.lockCancel)

        self.deleteButton_2.clicked.connect(self.deleteFeature)

        self.Transparency.setRange(0,100)
        self.Transparency.sliderReleased.connect(self.setTransparency)

        self.outlineSize.setRange(25,200)
        self.outlineSize.sliderReleased.connect(self.setOutlineSize)

        self.Size.sliderReleased.connect(self.setSize)
        self.color.clicked.connect(self.openColorDialog)
        self.Textinput.editingFinished.connect(self.getText)
        self.LineColor.clicked.connect(self.openLineColorDialog)

        listStyle=["Continua","Tratteggiata","Punteggiata","Tratto e Punto","Tratti e doppi Punti"]
        self.StyleLine.insertItems(0,listStyle)
        self.StyleLine.currentIndexChanged.connect(self.sendStyleLine)

        self.StyleList.currentIndexChanged.connect(self.sendStyleList)
        self.radioNew.toggled.connect(self.setFeatures)

        self.checkFillTransparency.stateChanged.connect(self.disablecolor)
        self.checkLineTransparency.stateChanged.connect(self.disableLineColor)

        self.radioGroup = QtGui.QButtonGroup()
        self.radioGroup.setExclusive(True)
        self.radioGroup.addButton(self.radioNew)
        self.radioGroup.addButton(self.radioList)

    def show(self):
        super(AnnotationDock, self).show()
        self.selectPoint()

    def closeAll(self,buttons):
        for x in buttons:
            x.hide()

    def showSelected(self,Tool):
        for x in Tool:
            x.show()

    def checkFalse(self,Tools):
        for x in Tools:
            x.setChecked(False)

    def appendTools(self,selected,toAppend):
        for x in toAppend:
            selected.append(x)

        return selected

    def selectPoint(self):
        self.PointButton.setChecked(True)
        self.closeAll(self.alldynacmic)
        self.StyleListFill()
        selectedTool = [self.StyleList,self.line_2]
        selectedTool=self.appendTools(selectedTool,self.showList)
        self.radioList.setChecked(True)
        self.deleteButton_2.setChecked(False)
        self.showSelected(selectedTool)
        self.selectMarker()
        RoamEvents.annoEdit.emit("drawPoint")
        super(AnnotationDock, self).resize(180,330)

    def selectPaint(self):
        self.paintButton.setChecked(True)
        self.closeAll(self.alldynacmic)
        self.StyleListFill()
        selectedTool = [self.StyleList,self.line_2]
        selectedTool=self.appendTools(selectedTool,self.showList)
        self.radioList.setChecked(True)
        self.deleteButton_2.setChecked(False)
        self.showSelected(selectedTool)
        RoamEvents.annoEdit.emit("drawPaint")
        super(AnnotationDock, self).resize(180,330)

    def selectLine(self):
        self.lineButton.setChecked(True)
        self.closeAll(self.alldynacmic)
        self.StyleListFill()
        selectedTool = self.OrizLine
        selectedTool=self.appendTools(selectedTool,self.drawTools)
        selectedTool=self.appendTools(selectedTool,self.showList)
        self.radioList.setChecked(True)
        self.showSelected(selectedTool)
        self.deleteButton_2.setChecked(False)
        self.LockUR()
        RoamEvents.annoEdit.emit("drawLine")
        super(AnnotationDock, self).resize(180,440)

    def selectPoly(self):
        self.polyButton.setChecked(True)
        self.closeAll(self.alldynacmic)
        self.StyleListFill()
        selectedTool = self.OrizLine
        selectedTool=self.appendTools(selectedTool,self.drawTools)
        selectedTool=self.appendTools(selectedTool,self.showList)
        self.radioList.setChecked(True)
        self.showSelected(selectedTool)
        self.deleteButton_2.setChecked(False)
        self.LockUR()
        RoamEvents.annoEdit.emit("drawPoly")
        super(AnnotationDock, self).resize(180,440)

    def selectRectangle(self):
        self.rectangleButton.setChecked(True)
        self.closeAll(self.alldynacmic)
        self.StyleListFill()
        selectedTool = self.OrizLine
        selectedTool=self.appendTools(selectedTool,self.drawTools)
        selectedTool=self.appendTools(selectedTool,self.showList)
        self.radioList.setChecked(True)
        self.showSelected(selectedTool)
        self.deleteButton_2.setChecked(False)
        self.LockUR()
        RoamEvents.annoEdit.emit("drawRectangle")
        super(AnnotationDock, self).resize(180,440)

    def selectCircle(self):
        self.circleButton.setChecked(True)
        self.closeAll(self.alldynacmic)
        self.StyleListFill()
        selectedTool = self.OrizLine
        selectedTool=self.appendTools(selectedTool,self.drawTools)
        selectedTool=self.appendTools(selectedTool,self.showList)
        self.radioList.setChecked(True)
        self.showSelected(selectedTool)
        self.deleteButton_2.setChecked(False)
        self.LockUR()
        RoamEvents.annoEdit.emit("drawCircle")
        super(AnnotationDock, self).resize(180,440)

    def chiudi(self):
        self.lockEndButton()
        self.resetDynamicDraw()
        RoamEvents.closeAnno.emit()
        super(AnnotationDock, self).close()

    def selectMarker(self):
        if self.checkFillTransparency.isEnabled() == False:
            self.checkFillTransparency.setChecked(False)
            self.checkFillTransparency.setEnabled(True)

        marker=""
        if self.regular_star.isChecked () == True:
            marker="regular_star"

        elif self.circle.isChecked () == True:
            marker="circle"

        elif self.diamond.isChecked () == True:
            marker="diamond"

        elif self.rectangle.isChecked () == True:
            marker="rectangle"

        elif self.cross.isChecked () == True:
            marker="cross2"
            self.checkFillTransparency.setChecked(True)
            self.checkFillTransparency.setEnabled(False)

        elif self.triangle.isChecked () == True:
            marker="triangle"

        elif self.filled_arrowhead.isChecked () == True:
            marker="filled_arrowhead"

        elif self.arrow.isChecked () == True:
            marker="arrow"

        elif self.pentagon.isChecked () == True:
            marker="pentagon"

        elif self.arrowhead.isChecked () == True:
            marker="arrowhead"
            self.checkFillTransparency.setChecked(True)
            self.checkFillTransparency.setEnabled(False)

        RoamEvents.sendMarker.emit(marker)

    def setTransparency(self):
        value=self.Transparency.sliderPosition()
        RoamEvents.setTransparency.emit(value)

    def setOutlineSize(self):
        value=self.outlineSize.sliderPosition()
        RoamEvents.setOutlineSize.emit(value)

    def setSize(self):
        value=self.Size.sliderPosition()
        RoamEvents.setSize.emit(value)

    def endEdit(self):
        RoamEvents.endEdit.emit()

    def unlockEndButton(self):
        self.endButton.setEnabled(True)

    def lockCancel(self):
        self.refreshButton.setEnabled(False)

    def lockEndButton(self):
        self.endButton.setEnabled(False)

    def UnlockUR(self):
        self.undoButton.setEnabled(True)
        self.redoButton.setEnabled(True)

    def LockUR(self):
        self.undoButton.setEnabled(False)
        self.redoButton.setEnabled(False)

    def callRefresh(self):
        RoamEvents.callRefresh.emit()
        self.refreshButton.setEnabled(False)

    def deleteFeature(self):
        selectedTool = self.alldynacmic
        selectedTool = self.appendTools(selectedTool,self.showList)
        self.closeAll(selectedTool)
        self.checkFalse(self.PrincipalTools)
        self.deleteButton_2.setChecked(True)
        super(AnnotationDock, self).resize(180,260)
        RoamEvents.annoEdit.emit("deleteFeature")

    def clickUndo(self):
        RoamEvents.clickUndoRedo.emit("undo")

    def clickRedo(self):
        RoamEvents.clickUndoRedo.emit("redo")

    def unlockCancelButton(self):
        self.refreshButton.setEnabled(True)

    def openColorDialog(self):
        color = QtGui.QColorDialog.getColor()

        if color.isValid():
            btn = self.sender()
            colHex=color.name()
            self.setButtobColor(btn,color)
            RoamEvents.sendColor.emit(colHex)

    def openLineColorDialog(self):
        color = QtGui.QColorDialog.getColor()

        if color.isValid():
            btn = self.sender()
            colHex=color.name()
            self.setButtobColor(btn,color)
            RoamEvents.sendLineColor.emit(colHex)

    def setButtobColor(self,btn,color):
        R=color.red()
        G=color.green()
        B=color.blue()
        stringa="QPushButton {background-color: rgb("+str(R)+", "+str(G)+", "+str(B)+') ;border:2px solid rgb(180, 180, 180);border-radius: 4px;font: bold 15pt "Arial";}QPushButton:hover{ background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa, stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);}'
        btn.setStyleSheet(stringa)

    def getText(self):
        text=self.Textinput.text()
        RoamEvents.sendText.emit(text)

    def sendStyleLine(self):
        style = self.StyleLine.currentIndex()
        RoamEvents.sendStyle.emit(style)

    def sendStyleList(self):
        listindex=self.StyleList.currentIndex()
        indexStyle = self.LabelIndex[listindex]
        RoamEvents.sendStyle.emit(int(indexStyle))

    def StyleListFill(self):
        vector_layer = self.checkLayer()
        render = vector_layer.rendererV2()
        categories = QgsCategorizedSymbolRendererV2.convertFromRenderer (render)
        categories_list=categories.categories()
        Label=[]
        self.StyleList.clear()
        self.LabelIndex = []
        ListValue=[]
        catList=[]
        catList=categories.legendSymbologyItems(QSize (40,40))

        i=0
        e=0
        for x in catList:
            ListValue = categories_list[e]
            for y in x:
                if i % 2 == 0:
                    Label.append(y)
                    self.LabelIndex.append(int(ListValue.value()))

                elif i % 2 == 1:
                    icon=QIcon(y)
                    self.StyleList.insertItem(e,icon,Label[e])
                i += 1
            e += 1

    def checkLayer(self):
        layer = ''

        if self.PointButton.isChecked () == True:
            layer = self.layerid[0]
        elif self.lineButton.isChecked () == True or self.paintButton.isChecked () == True:
            layer = self.layerid[1]
        else:
            layer = self.layerid[2]

        vector_layer = QgsMapLayerRegistry.instance().mapLayer(layer)
        return vector_layer

    def setFeatures(self):
        self.resetDynamicDraw()

        if self.radioNew.isChecked () == True:
            self.StyleList.hide()

            if self.lineButton.isChecked () == True:
                selectedTool = self.LineToshow
                self.showSelected(selectedTool)
                self.Size.setRange(25,200)
                self.Size.setSliderPosition(0)
                super(AnnotationDock, self).resize(180,570)

            elif self.paintButton.isChecked () == True:
                selectedTool = self.LineToshow
                selectedTool.append(self.OrizLine[0])
                self.showSelected(selectedTool)
                self.Size.setRange(25,200)
                self.Size.setSliderPosition(0)
                super(AnnotationDock, self).resize(180,460)

            elif self.PointButton.isChecked () == True:
                selectedTool = self.PoinToshow
                selectedTool = self.appendTools(selectedTool,self.LineToshow)
                self.showSelected(selectedTool)
                self.Size.setRange(100,1500)
                self.Size.setTickInterval(50)
                self.regular_star.setChecked(True)
                super(AnnotationDock, self).resize(180,640)

            else:
                selectedTool=[]
                selectedTool = self.PoinToshow
                selectedTool=self.appendTools(selectedTool,self.LineToshow)
                self.showSelected(selectedTool)
                self.scrollAreaMarker.hide()
                self.Size.hide()
                self.regular_star.setChecked(True)
                super(AnnotationDock, self).resize(180,660)

            RoamEvents.sendCheckRadio.emit("New")
        else:
            if self.lineButton.isChecked () == True:
                self.selectLine()

            elif self.paintButton.isChecked () == True:
                self.selectPaint()

            elif self.PointButton.isChecked () == True:
                self.selectPoint()

            else:
                if self.polyButton.isChecked () == True:
                    self.selectPoly()

                elif self.rectangleButton.isChecked () == True:
                    self.selectRectangle()

                elif self.circleButton.isChecked () == True:
                    self.selectCircle()

            RoamEvents.sendCheckRadio.emit("List")

    def addList(self):
        self.radioList.setChecked(True)
        self.StyleList.setCurrentIndex(self.StyleList.count()-1)

    def disablecolor(self):
        if self.checkFillTransparency.isChecked () == True:
            self.color.setEnabled(False)
            self.color.setStyleSheet('QPushButton {background-color:transparent;border:2px  solid rgb(180, 180, 180);border-radius: 4px;font: bold 15pt "Arial";}QPushButton:hover{ background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa, stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);}')
            RoamEvents.sendColor.emit('')
        else:
            self.color.setEnabled(True)

    def disableLineColor(self):
        if self.checkLineTransparency.isChecked () == True:
            self.LineColor.setEnabled(False)
            self.LineColor.setStyleSheet('QPushButton {background-color: rgb(0, 0, 0, 0);border:2px solid rgb(180, 180, 180);border-radius: 4px;font: bold 15pt "Arial";}QPushButton:hover{ background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa, stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);}')
            RoamEvents.sendLineColor.emit('')
        else:
            self.LineColor.setEnabled(True)
            self.LineColor.setStyleSheet('QPushButton {background-color: rgb(0, 0, 0);border:2px solid rgb(180, 180, 180);border-radius: 4px;font: bold 15pt "Arial";}QPushButton:hover{ background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa, stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);}')
    def resetDynamicDraw(self):
        self.Textinput.clear()
        self.Transparency.setSliderPosition(0)
        self.Size.setSliderPosition(0)
        self.StyleLine.setCurrentIndex(0)
        self.color.setStyleSheet('QPushButton {background-color:transparent;border:2px  solid rgb(180, 180, 180);border-radius: 4px;font: bold 15pt "Arial";}QPushButton:hover{ background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa, stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);}')
        self.LineColor.setStyleSheet('QPushButton {background-color: rgb(0,0,0);border:2px solid rgb(180, 180, 180);border-radius: 4px;font: bold 15pt "Arial";}QPushButton:hover{ background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa, stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);}')
        self.checkFillTransparency.setChecked(False)
        self.checkLineTransparency.setChecked(False)
        self.outlineSize.setSliderPosition(0)
        self.checkFillTransparency.setEnabled(True)
        self.Size.setTickInterval(10)
