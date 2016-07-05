from qgis.core import QGis

from roam.maptools.maptools import PointTool, PolygonTool, PolylineTool
from roam.maptools.inspectiontool import InspectionTool
from roam.maptools.movetool import MoveTool
from roam.maptools.edittool import EditTool
from roam.maptools.infotool import InfoTool
from roam.maptools.touchtool import TouchMapTool
from roam.maptools.annotationtool import AnnotationTool

tools = {QGis.Point: PointTool,
         QGis.Polygon: PolygonTool,
         QGis.Line: PolylineTool}

