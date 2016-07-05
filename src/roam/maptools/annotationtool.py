from collections import OrderedDict
from roam.maptools.maptool import MapTool
from roam.maptools.touchtool import TouchMapTool
from roam.maptools import maptoolutils
from roam.api.events import RoamEvents
from roam.utils import log
from roam.maptools import MoveTool, EditTool, PointTool, TouchMapTool
from roam.api.events import RoamEvents
from pyspatialite import dbapi2
from PyQt4.QtCore import *
from PyQt4.QtGui import QColor, QMessageBox, QIcon
from PyQt4 import QtGui
from qgis.core import *
from qgis.gui import *
import roam.resources_rc
from math import *
import glob
import os

class AnnotationTool(QgsMapTool):
    def __init__(self, canvas, snapradius = 2):
        super(AnnotationTool, self).__init__(canvas)
        self.canvas = canvas
        self.setRubber()
        self.selectrect = QRect()
        self.selectband = None
        RoamEvents.annoEdit.connect(self.selecTool)
        RoamEvents.sendMarker.connect(self.selectMarker)
        RoamEvents.endEdit.connect(self.endEditDraw)
        RoamEvents.closeAnno.connect(self.closeAnnotation)
        RoamEvents.callRefresh.connect(self.refresh)
        RoamEvents.clickUndoRedo.connect(self.UndoRedoCicked)
        RoamEvents.setTransparency.connect(self.setTransparency)
        RoamEvents.setSize.connect(self.setSize)
        RoamEvents.setOutlineSize.connect(self.setOutlineSize)
        RoamEvents.sendColor.connect(self.setColor)
        RoamEvents.sendText.connect(self.setText)
        RoamEvents.sendStyle.connect(self.setStyle)
        RoamEvents.sendCheckRadio.connect(self.setCheckRadio)
        RoamEvents.sendLineColor.connect(self.setLineColor)
        self.layerid=["point20150114085613922","line20150114085613640","polygon20150114085614076"]
        self.points=[]
        self.firstpoint = ""
        self.rucount=0
        self.rectpointcount = 0
        self.securePoints=[]
        self.savepoints = []
        self.undoRedo = ""
        self.transparency=0
        self.size=0.25
        self.color=''
        self.label = ''
        self.border_color='#000000'
        self.Style = "solid"
        self.checkRadio = "List"
        self.Marker = "regular_star"
        self.outline_width = 0.25

    def canvasPressEvent(self, event):
        if event.button() == Qt.RightButton:
            return
        self.selectrect.setRect( 0, 0, 0, 0 )
        self.selectband = QgsRubberBand(self.canvas, QGis.Polygon )
        self.selectband.setColor(QColor.fromRgb(0,0,255, 65))
        self.selectband.setWidth(5)
        x = event.pos().x()
        y = event.pos().y()

        if self.drawTool == "drawPaint":
            self.firstpoint = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.band.addPoint(point)


    def canvasMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()

        if self.drawTool == "drawLine" and self.firstpoint != "":
            point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.rubberline(point)

        elif self.drawTool == "drawPaint" and self.firstpoint != "":
            point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.band.addPoint(point)
            self.securePoints.append(point)

        elif self.drawTool == "drawPoly" and self.firstpoint != "":
            point=self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.rubberpoly(point)

        elif self.drawTool == "drawRectangle":
            point=self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.rubbeRectangle(point)
            if len(self.securePoints)>1:
                RoamEvents.unlockEndEdit.emit()

        elif self.drawTool == "drawCircle":
            point=self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.rubbeCircle(point)
            if len(self.securePoints)>0:
                RoamEvents.unlockCancel.emit()
                RoamEvents.unlockEndEdit.emit()

    def canvasReleaseEvent(self, event):

        if event.button() == Qt.RightButton:
            if self.drawTool != "drawPaint":
                self.endEditDraw()

        else:
            x = event.pos().x()
            y = event.pos().y()

            point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.firstpoint = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
            self.securePoints.append(point)
            self.lastpoint= point
            self.savepoints=[]

            if len(self.securePoints) > 0:
                RoamEvents.unlockUndoRedo.emit()
                RoamEvents.unlockCancel.emit()

            if self.drawTool == "drawLine":
                self.points.append(point)
                self.pointband.addPoint(point)
                self.band.addPoint(point)
                if len(self.securePoints) > 1:
                    RoamEvents.unlockEndEdit.emit()

            elif self.drawTool == "drawPoly":
                self.points.append(point)
                self.pointband.addPoint(point)
                self.polyband.addPoint(point)
                if len(self.securePoints) > 2:
                    RoamEvents.unlockEndEdit.emit()

            elif self.drawTool == "drawRectangle":
                self.points.append(point)
                self.rectpointcount += 1

                self.pointband.addPoint(point)
                self.rectband.addPoint(point)

                if len(self.securePoints) == 3:
                    RoamEvents.unlockEndEdit.emit()
                    self.endEditDraw()

            elif self.drawTool == "drawCircle":
                self.points.append(point)
                self.pointband.addPoint(point)
                self.polyband.addPoint(point)
                if len(self.securePoints) == 2:
                    RoamEvents.unlockEndEdit.emit()
                    self.endEditDraw()

            elif self.drawTool=="drawPoint":
                self.drawPointTool(point)

            elif self.drawTool=="drawPaint":
                self.endEditDraw()

            elif self.drawTool=="deleteFeature":
                self.deleteFeature(event, point)


    def setRubber(self):
        self.polyband = QgsRubberBand(self.canvas, QGis.Polygon )
        self.polyband.setColor(QColor.fromRgb(0,65,105,225))
        self.polyband.setWidth(5)
        self.band = QgsRubberBand(self.canvas)
        self.band.setColor(QColor.fromRgb(65,105,225))
        self.band.setWidth(5)
        self.pointband = QgsRubberBand(self.canvas, QGis.Point)
        self.pointband.setColor(QColor.fromRgb(0,0,255, 100))
        self.pointband.setIconSize(10)
        self.rectband = QgsRubberBand(self.canvas, QGis.Polygon )
        self.rectband.setColor(QColor.fromRgb(0,65,105,225))
        self.rectband.setWidth(5)

    def setTransparency(self,value):
        self.transparency=value

    def setSize(self,value):
        self.size=value * 0.01

    def setOutlineSize(self,value):
        self.outline_width = value * 0.01

    def setColor(self,value):
        self.color=value

    def setLineColor(self,value):
        self.border_color=value

    def setText(self,value):
        self.label = value

    def setCheckRadio(self,value):
        self.checkRadio = value

    def setStyle(self,value):
        if self.checkRadio == "List":
            self.ListIndex = value

        elif self.checkRadio == "New":
            if value == 0:
                self.Style = "solid"
            elif value == 1:
                self.Style = "dash"
            elif value == 2:
                self.Style = "dot"
            elif value == 3:
                self.Style = "dash dot"
            elif value == 4:
                self.Style = "dash dot dot"

    def resetRubber(self):
        self.band.reset()
        self.pointband.reset()
        self.polyband.reset()
        self.rectband.reset()
        self.setRubber()
        self.securePoints=[]
        self.savepoints = []
        self.undoRedo = ""
        RoamEvents.lockUndoRedo.emit()

    def resetFeatures(self):
        self.points=[]
        self.firstpoint = ""
        self.layer = ""
        self.rucount = 0
        self.rectpointcount = 0

    def refresh(self):
        self.resetRubber()
        self.resetFeatures()
        RoamEvents.lockEndEdit.emit()

    def resetDynamic(self):
        self.color=''
        self.label = ''
        self.border_color='#000000'
        self.Style = "solid"
        self.transparency=0
        self.size=0.25
        self.Marker = "regular_star"
        self.outline_width = 0.25

    def UndoRedoCicked (self,tool):
        if tool == "undo":
            if len(self.securePoints)>0:
                RoamEvents.unlockCancel.emit()

            if self.drawTool == "drawLine" and len(self.securePoints)>0:
                self.UndoLine()
                if len(self.securePoints) < 2:
                    RoamEvents.lockEndEdit.emit()

            elif self.drawTool == "drawPoly" and len(self.securePoints)>0:
                self.UndoPolygon()

                if len(self.securePoints) < 3:
                    RoamEvents.lockEndEdit.emit()

            elif self.drawTool == "drawRectangle" and len(self.securePoints)>0:
                self.UndoRectangle()
                if len(self.securePoints) < 2:
                    RoamEvents.lockEndEdit.emit()


            elif self.drawTool == "drawCircle" and len(self.securePoints)>0:
                self.UndoCircle()
                if len(self.securePoints) < 2:
                    RoamEvents.lockEndEdit.emit()

        elif tool == "redo" and len(self.savepoints)>0 :
            if len(self.securePoints)>0:
                RoamEvents.unlockCancel.emit()

            if self.drawTool == "drawLine":
                self.RedoLine()
                if len(self.securePoints)>1:
                    RoamEvents.unlockEndEdit.emit()

            elif self.drawTool == "drawPoly":
                self.RedoPolygon()
                if len(self.securePoints)>2:
                    RoamEvents.unlockEndEdit.emit()

            elif self.drawTool == "drawRectangle":
                self.RedoRectangle()

            elif self.drawTool == "drawCircle":
                self.RedoCircle()

    def UndoLine (self):
        x=self.band.numberOfVertices()
        while x > (len(self.securePoints)):
            self.band.removeLastPoint(0,True)
            x=self.band.numberOfVertices()

        if len(self.securePoints) == 1:
            self.pointband.removeLastPoint(0,True)

        self.pointband.removeLastPoint(0,True)
        self.lastpoint = self.securePoints.pop()
        self.savepoints.append(self.lastpoint)

    def RedoLine(self):
        localpoint = self.savepoints[-1]
        self.savepoints.pop()
        self.band.removeLastPoint(0,True)
        self.pointband.addPoint(localpoint)
        self.securePoints.append(localpoint)
        self.band.addPoint(localpoint)
        self.band.addPoint(localpoint)

    def UndoPolygon (self):
        x=self.polyband.numberOfVertices()
        while x > (len(self.securePoints)):
            self.polyband.removeLastPoint(0,True)
            x=self.polyband.numberOfVertices()

        if len(self.securePoints) == 1:
            self.pointband.removeLastPoint(0,True)

        self.pointband.removeLastPoint(0,True)
        self.lastpoint = self.securePoints.pop()
        self.savepoints.append(self.lastpoint)

    def RedoPolygon(self):
        localpoint = self.savepoints[-1]
        self.savepoints.pop()
        self.polyband.removeLastPoint(0,True)
        self.pointband.addPoint(localpoint)
        self.securePoints.append(localpoint)
        self.polyband.addPoint(localpoint)
        self.polyband.addPoint(localpoint)

    def UndoRectangle (self):

        if len(self.securePoints) == 2:
            self.rectband.removeLastPoint(0,True)
            self.rectband.removeLastPoint(0,True)
            self.rectband.removeLastPoint(0,True)
            self.rectpointcount = 2

        elif len(self.securePoints) == 1:
            self.rectband.removeLastPoint(0,True)
            self.rectband.removeLastPoint(0,True)
            self.rectpointcount = 0

        elif len(self.securePoints) == 1:
            self.pointband.removeLastPoint(0,True)

        self.pointband.removeLastPoint(0,True)
        self.lastpoint = self.securePoints.pop()
        self.savepoints.append(self.lastpoint)

    def RedoRectangle(self):
        localpoint = self.savepoints[-1]
        self.savepoints.pop()
        self.rectband.removeLastPoint(0,True)

        if len(self.securePoints) == 1:
            self.rectpointcount = 3

        elif len(self.securePoints) == 0:
            self.rectpointcount = 1

        self.pointband.addPoint(localpoint)
        self.securePoints.append(localpoint)
        self.rectband.addPoint(localpoint)
        self.rectband.addPoint(localpoint)

    def UndoCircle(self):
        self.lastpoint = self.securePoints.pop()
        self.savepoints.append(self.lastpoint)
        self.polyband.reset()
        self.pointband.removeLastPoint(0,True)
        self.pointband.removeLastPoint(0,True)

    def RedoCircle(self):
        localpoint = self.savepoints.pop()
        self.pointband.addPoint(localpoint)
        self.polyband.addPoint(localpoint)
        self.securePoints.append(localpoint)

    def rubberpaint(self,point):
        self.band.addPoint(point)

    def rubberline(self,point):
        if self.rucount == 0:
            self.band.addPoint(self.firstpoint)
            self.band.addPoint(point)
            self.rucount=1

        else:
            self.band.removePoint(-1,True)
            self.band.addPoint(point)

    def rubberpoly(self,point):
        if self.rucount == 0:
            self.polyband.addPoint(self.firstpoint)
            self.polyband.addPoint(point)
            self.rucount=1

        else:
            self.polyband.removePoint(-1,True)
            self.polyband.addPoint(point)

    def rubbeRectangle(self,point):

        if self.rectpointcount == 1 :
            self.rectband.addPoint(point)
            self.rectpointcount = 2

        if self.rectpointcount == 2 :
            self.rectband.removePoint(-1,True)
            self.rectband.addPoint(point)

        if self.rectpointcount > 2 :

            p1 = self.securePoints[0]
            p2 = self.securePoints[1]
            p3=point
            angle_exist = self.calcAngleExistant(p1,p2)
            side = self.calc_isCollinear(p1, p2, p3) # check if x_p2 > x_p1 and inverse side
            if side == 0:
                return None

            if p1.x() < p2.x():
                side *= -1

            length = QgsDistanceArea().measureLine(p2, p3) * side
            p3 = QgsPoint(p2.x() + length * cos(radians(90) + angle_exist), p2.y() + length * sin(radians(90) + angle_exist))

            length = QgsDistanceArea().measureLine(p2, p3) * side
            p4 = QgsPoint(p1.x() + length * cos(radians(90) + angle_exist), p1.y() + length * sin(radians(90) + angle_exist))

        if self.rectpointcount == 3 :

            self.rectband.addPoint(p3)
            self.rectband.addPoint(p4)
            self.rectpointcount = 4

        if self.rectpointcount == 4 :

            self.rectband.removePoint(-1,True)
            self.rectband.removePoint(-1,True)
            self.rectband.addPoint(p3)
            self.rectband.addPoint(p4)

    def rubbeCircle(self,point):
        if len(self.securePoints) > 0:
            segments=36
            pc=self.securePoints[0]
            p1=point
            circle = QgsGeometry.fromPoint(pc).buffer(QgsDistanceArea().measureLine(pc, p1), segments)
            self.polyband.setToGeometry(circle, None)

    def endEditDraw(self):
        Points=self.securePoints

        self.resetRubber()
        self.resetFeatures()

        if self.drawTool=="drawLine":
            if len(Points)>1:
                self.drawLineTool(Points)

        elif self.drawTool=="drawPaint":
            if len(Points)>1:
                 self.drawPaintTool(Points)

        elif self.drawTool=="drawPoly":
            if len(Points)>2:
                self.drawPolyTool(Points)

        elif self.drawTool=="drawRectangle":
            if len(Points)==3:
                self.drawRectangleTool(Points)

        elif self.drawTool=="drawCircle":
            if len(Points)==2:
                self.drawCircleTool(Points)

        RoamEvents.lockEndEdit.emit()
        RoamEvents.lockCancel.emit()

    def selecTool(self, tool):
        self.drawTool= tool
        self.resetRubber()
        self.resetFeatures()
        self.resetDynamic()
        RoamEvents.lockEndEdit.emit()
        RoamEvents.lockCancel.emit()

    def selectMarker(self,marker):
        self.Marker = marker

    def drawPointTool (self,point):
        self.layer = QgsMapLayerRegistry.instance()
        self.pointLayer=self.layer.mapLayer(self.layerid[0])
        pr = self.pointLayer.dataProvider()

        if self.checkRadio == "New":
            value=self.set_vector_categorized_style(self.pointLayer)
        else:
            value=self.ListIndex

        pt = QgsFeature()
        pt.setGeometry(QgsGeometry.fromPoint(point))
        pt.setAttributes([None,value])
        pr.addFeatures([pt])
        self.pointLayer.updateExtents()
        self.canvas.refresh()
        self.resetFeatures()

        if self.checkRadio == "New":
            RoamEvents.addList.emit()
            self.resetDynamic()

    def drawPaintTool(self,points):
        Points=points
        self.layer = QgsMapLayerRegistry.instance()
        self.paintLayer=self.layer.mapLayer(self.layerid[1])
        pr = self.paintLayer.dataProvider()

        if self.checkRadio == "New":
            value=self.set_vector_categorized_style(self.paintLayer)
        else:
            value=self.ListIndex

        line = QgsFeature()
        line.setAttributes([None,value])
        line.setGeometry(QgsGeometry.fromPolyline(Points))
        pr.addFeatures([line])
        self.paintLayer.updateExtents()
        self.canvas.refresh()
        self.resetFeatures()

        if self.checkRadio == "New":
            RoamEvents.addList.emit()
            self.resetDynamic()

    def drawLineTool (self,points):
        Points=points
        self.layer = QgsMapLayerRegistry.instance()
        self.lineLayer=self.layer.mapLayer(self.layerid[1])
        pr = self.lineLayer.dataProvider()

        if self.checkRadio == "New":
            value=self.set_vector_categorized_style(self.lineLayer)
        else:
            value=self.ListIndex

        line = QgsFeature()
        line.setAttributes([None,value])
        line.setGeometry(QgsGeometry.fromPolyline(Points))
        pr.addFeatures([line])
        self.lineLayer.updateExtents()
        self.canvas.refresh()
        self.resetFeatures()

        if self.checkRadio == "New":
            RoamEvents.addList.emit()
            self.resetDynamic()

    def drawPolyTool (self,points):
        Points=points
        fpoint=Points[0]
        Points.append(fpoint)
        self.layer = QgsMapLayerRegistry.instance()
        self.polyLayer=self.layer.mapLayer(self.layerid[2])
        pr = self.polyLayer.dataProvider()

        if self.checkRadio == "New":
            value=self.set_vector_categorized_style(self.polyLayer)
        else:
            value=self.ListIndex

        poly = QgsFeature()
        poly.setAttributes([None,value])
        poly.setGeometry(QgsGeometry.fromPolygon([Points]))
        pr.addFeatures([poly])
        self.polyLayer.updateExtents()
        self.canvas.refresh()
        self.resetFeatures()

        if self.checkRadio == "New":
            RoamEvents.addList.emit()
            self.resetDynamic()

    def drawRectangleTool (self,points):
        Points=points
        p1=Points[0]
        p2=Points[1]
        p3=Points[2]
        angle_exist = self.calcAngleExistant(p1, p2)

        side = self.calc_isCollinear(p1, p2, p3) # check if x_p2 > x_p1 and inverse side
        if side == 0:
            return None

        if p1.x() < p2.x():
            side *= -1
        length = QgsDistanceArea().measureLine(p2, p3) * side
        p3 = QgsPoint(p2.x() + length * cos(radians(90) + angle_exist), p2.y() + length * sin(radians(90) + angle_exist))
        p4 = QgsPoint(p1.x() + length * cos(radians(90) + angle_exist), p1.y() + length * sin(radians(90) + angle_exist))
        rectanglePoints=[p1,p2,p3,p4]

        self.layer = QgsMapLayerRegistry.instance()
        self.polyLayer=self.layer.mapLayer(self.layerid[2])
        pr = self.polyLayer.dataProvider()

        if self.checkRadio == "New":
            value=self.set_vector_categorized_style(self.polyLayer)
        else:
            value=self.ListIndex

        rectangle = QgsFeature()
        rectangle.setAttributes([None,value])
        rectangle.setGeometry(QgsGeometry.fromPolygon([rectanglePoints]))
        pr.addFeatures([rectangle])
        self.polyLayer.updateExtents()
        self.canvas.refresh()
        self.resetFeatures()

        if self.checkRadio == "New":
            RoamEvents.addList.emit()
            self.resetDynamic()

    def drawCircleTool (self,points,segments=36):
        pc=points[0]
        p1=points[1]
        circle = QgsGeometry.fromPoint(pc).buffer(QgsDistanceArea().measureLine(pc, p1), segments)
        self.layer = QgsMapLayerRegistry.instance()
        self.polyLayer=self.layer.mapLayer(self.layerid[2])
        pr = self.polyLayer.dataProvider()

        if self.checkRadio == "New":
            value=self.set_vector_categorized_style(self.polyLayer)
        else:
            value=self.ListIndex

        fcircle = QgsFeature()
        fcircle.setAttributes([None,value])
        fcircle.setGeometry(circle)
        pr.addFeatures([fcircle])
        self.polyLayer.updateExtents()
        self.canvas.refresh()
        self.resetFeatures()

        if self.checkRadio == "New":
            RoamEvents.addList.emit()
            self.resetDynamic()

    def calcAngleExistant(self, p1, p2):
        a = self.calcPente(p1, p2) # The slope of the segment p1-p2
        length_p1p2 = QgsDistanceArea().measureLine(p1, p2) # Hypothenuse
        length_adjacent = fabs(p2.y() - p1.y()) # Adjacent
        if length_p1p2 == 0: # Normally you can't have a length of 0 but avoid division by zero
            angle_CAB = 0
        else:
            angle_CAB = acos(length_adjacent/length_p1p2) #

        # Correction of angle_CAB
        if a<0:
            angle_CAB = angle_CAB - pi/2
        elif a>0:
            angle_CAB = pi/2 - angle_CAB

        return angle_CAB

    def calc_isCollinear(self,p0, p1, pCherche):
        sens =  (   ( pCherche.x() - p0.x() ) * (p1.y() - p0.y() ) - \
                    ( pCherche.y() - p0.y() ) * (p1.x() - p0.x() ) )

        if sens > 0:
            return 1

        elif sens < 0:
            return -1

        else:
            return 0

    def calcPente(self,p1, p2):
        """
        Return the slope of the line represents by two points : p1 and p2
        :param p1: The first point
        :param p2: The second point
        :type p1: QgsPoint
        :type p2: QgsPoint
        :return: Return the slope (degre)
        :rtype: float
        """

        num = p1.x() - p2.x()
        denum = p1.y() - p2.y()

        # Avoid division by zero
        if num == 0:
            # Return a negative value if denum > 0
            if denum > 0:
                return -90
            else:
            # else return a positive value
                return 90
        # Same as above with denum
        elif denum == 0:
            if num > 0:
                return -90
            else:
                return 90
        else:
            return denum/num

    def closeAnnotation(self):
        self.resetRubber()

    def deleteFeature(self, event, point):
        def conferma(text):
            msgBox=QMessageBox()
            msgBox.setText(text)
            msgBox.addButton(QMessageBox.Yes)
            msgBox.addButton(QMessageBox.No)
            msgBox.setWindowTitle("IntraMaps Roam")
            icon = QIcon(":/icons/info")
            msgBox.setWindowIcon(icon)
            ret = msgBox.exec_()
            if ret==QMessageBox.Yes:
                return True
            else:
                return False
        rect = self.toSearchRect(event.pos())
        results = OrderedDict((l,f) for l, f in self.getFeatures(rect))
        for l, f in results.items():
            for fItem in f:
                l.select(fItem.id())
                if conferma("Eliminare la feature selezionata?"):
                    l.startEditing()
                    l.deleteFeature(fItem.id())
                    l.commitChanges()
                else:
                    l.deselect(fItem.id())

    def getFeatures(self, rect, firstonly=False):
        # The MS SQL driver seems to crash with a empty rectangle.
        # Need to check QGIS to patch issue
        if rect.isEmpty():
            return
        layersname = ['annotation_point','annotation_line','annotation_polygon']
        selectionlayers = layersfromlist(layersname)
        #self.layer = QgsMapLayerRegistry.instance()
        #self.pointLayer=self.layer.mapLayer(self.layerid[0])
        #pr = self.pointLayer.dataProvider()


        for layer in selectionlayers.itervalues():
            if (not layer.type() == QgsMapLayer.VectorLayer or
                    layer.geometryType() == QGis.NoGeometry):
                continue

            rect = self.toLayerCoordinates(layer, rect)
            rq = QgsFeatureRequest().setFilterRect(rect) \
                .setFlags(QgsFeatureRequest.ExactIntersect)
            features = []
            for feature in layer.getFeatures(rq):
                if feature.isValid():
                    features.append(feature)

            yield layer, features

    def toSearchRect(self, point):
        size = 5
        rect = QRectF()
        rect.setLeft(point.x() - size)
        rect.setRight(point.x() + size)
        rect.setTop(point.y() - size)
        rect.setBottom(point.y() + size)

        transform = self.canvas.getCoordinateTransform()
        ll = transform.toMapCoordinates(rect.left(), rect.bottom())
        ur = transform.toMapCoordinates(rect.right(), rect.top())

        rect = QgsRectangle(ur, ll)
        return rect


    def set_vector_categorized_style(self,vector_layer):
        filename=glob.glob('*.qgs')
        path=os.getcwd()
        proj=os.path.join(path,filename[0])

        text=self.readProject(proj)
        legend=self.extractlegend(text)
        geometry_type = vector_layer.geometryType()

        if self.color == "":
            polymeta = "SimpleLine"
            colour = QtGui.QColor(0,0,0,0)
        else:
            polymeta = "SimpleFill"
            colour = QtGui.QColor(self.color)

        if self.border_color == "":
            LineColorRGB = "0,0,0,0"
            LineColor = "0,0,0,0"
        else:
            LineColor = QtGui.QColor(self.border_color)
            LineColorRGB = self.setRGBcolor(LineColor)

        # Transparency 100: transparent
        # Transparency 0: opaque
        transparency_percent=self.transparency
        alpha = 1 - transparency_percent / 100.0
        size=self.size

        registry = QgsSymbolLayerV2Registry.instance()
        symbol = QgsSymbolV2.defaultSymbol(geometry_type)
        render = vector_layer.rendererV2()
        categories = QgsCategorizedSymbolRendererV2.convertFromRenderer (render)
        value=self.checkDB(categories)
        value += 1

        label = self.label
        if label.strip() == '':
            label='Style_'+str(value)

        # We need to create a custom symbol layer as
        # the border colour of a symbol can not be set otherwise
        # noinspection PyArgumentList
        if geometry_type == QGis.Point:
            markerMeta = registry.symbolLayerMetadata("SimpleMarker")
            # Marker layer
            pointLayer = markerMeta.createSymbolLayer({'name': self.Marker, 'color_border': LineColorRGB,'outline_width':str(self.outline_width),'outline_style':self.Style, 'angle': '0'})
            symbol.deleteSymbolLayer(0)
            symbol.appendSymbolLayer(pointLayer)
            symbol.setSize(size)
            symbol.setColor(colour)
            symbol.setAlpha(alpha)

        elif geometry_type == QGis.Polygon:
            if polymeta == "SimpleLine":
                #colour=LineColor
                colour = QtGui.QColor(LineColor)

            polyMeta = registry.symbolLayerMetadata(polymeta)
            polyLayer = polyMeta.createSymbolLayer({'line_style': self.Style, 'line_color': LineColorRGB, 'line_width': str(self.outline_width)})
            symbol.deleteSymbolLayer(0)
            symbol.appendSymbolLayer(polyLayer)
            symbol.setColor(colour)
            symbol.setAlpha(alpha)

        elif geometry_type == QGis.Line:
            lineMeta = registry.symbolLayerMetadata("SimpleLine")
            # Line layer
            lineLayer = lineMeta.createSymbolLayer({'penstyle': self.Style, 'use_custom_dash': '0', 'joinstyle': 'bevel', 'capstyle': 'square'})
            symbol.deleteSymbolLayer(0)
            symbol.appendSymbolLayer(lineLayer)
            symbol.setWidth(size)
            symbol.setColor(LineColor)
            symbol.setAlpha(alpha)

        category = QgsRendererCategoryV2(value, symbol, label)
        categories.addCategory(category)
        vector_layer.setRendererV2(categories)
        vector_layer.saveDefaultStyle()
        project = QFileInfo(proj)
        QgsProject.instance().write(project)
        self.adjustProject(proj,legend)
        return value

    def checkDB(self,categories):
        categories_list=categories.categories()
        value=[]
        for x in categories_list:
            value.append(int(x.value()))

        maxval = max(value)
        return maxval

    def readProject(self,proj):
        fopen=open(proj,"r")
        text=fopen.readlines()
        fopen.close()
        return text

    def extractlegend (self,text):
        Fsearch='    </mapcanvas>\n'
        Lsearch='    </legend>\n'
        Findex=0
        Lindex=0
        legend=[]

        for x in text:
            if x==Fsearch:
                Findex=text.index(Fsearch)
                break

        Findex += 1

        for x in text:
            if x==Lsearch:
                Lindex=text.index(Lsearch)
                break

        Lindex += 1

        for x in range(Findex,Lindex):
            legend.append(text[x])

        return legend

    def adjustProject(self,proj,legend):
        search='    </mapcanvas>\n'
        indice=0
        text=self.readProject(proj)

        for x in text:
            if x==search:
                indice=text.index(search)
                break

        for x in legend:
            indice += 1
            text.insert(indice,x)

        fopen=open(proj,"w")
        fopen.writelines(text)
        fopen.close()

    def setRGBcolor(self,LineColor):
        R = LineColor.red()
        G = LineColor.green()
        B = LineColor.blue ()
        LineColorRGB = str(R)+","+str(G)+","+str(B)
        return LineColorRGB

def layersfromlist(layerlist):
    """
    Transform a list of layer names into layer objects from the layer registry.
    :param layerlist:
    :return:
    """
    qgislayers = QgsMapLayerRegistry.instance().mapLayers().values()
    qgislayers = {layer.name(): layer for layer in qgislayers if layer.type() == QgsMapLayer.VectorLayer}
    if not layerlist:
        return qgislayers
    else:
        _qgislayers = OrderedDict()
        for layername in layerlist:
            try:
                _qgislayers[layername] = qgislayers[layername]
            except KeyError:
                continue
        return _qgislayers
