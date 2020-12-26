"""Point Structure."""
from rules.drawable import *
polygonADT = {
    is_a:tuple(),
    "new":{
        (list, Point,):{
            args:("listOfPoints",),
            trgt:Polygon.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Polygon.fromLines,
        },
        retVal:Polygon
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Polygon.fromPolygon
        },
        retVal:Polygon
    },
    "area":{
        tuple():{
            args:tuple(),
            trgt:Polygon.area
        },
        retVal:float
    },
    "get_indexed_point":{
        (float,):{
            args:("idx",),
            trgt:Polygon.getIndexedPoint
        },
        retVal:Point
    },
    "get_indexed_line":{
        (float,):{
            args:("idx",),
            trgt:Polygon.getIndexedLine
        },
        retVal:Line
    },
    "signed_area":{
        tuple():{
            args:tuple(),
            trgt:Polygon.signedArea
        },
        retVal:float
    },
    "centroid":{
        tuple():{
            args:tuple(),
            trgt:Polygon.centroid
        },
        retVal:Point
    },
    "vertex_centroid":{
        tuple():{
            args:tuple(),
            trgt:Polygon.vertexCentroid
        },
        retVal:Point
    },
    "internal_angle":{
        (float,):{
            args:("idx",),
            trgt:Polygon.internAngle
        },
        (Point,):{
            args:("point",),
            trgt:Polygon.internAngle
        },
        retVal:float
    },
    "angle_bisector":{
        (float,):{
            args:("idx",),
            trgt:Polygon.angleBisector
        },
        (Point,):{
            args:("point",),
            trgt:Polygon.angleBisector
        },
        retVal:Line
    }
}