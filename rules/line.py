"""Point Structure."""
from rules.drawable import *
lineADT = {
    "is_a":None,
    "new":{
        (Point,Point,):{
            args:("point1","point2"),
            trgt:Line.fromPoints,
        },
        (float,float,Point,):{
            args:("angle","length","point",),
            trgt:Line.fromMetrics,
        },
        ret:Point
    },
    "copy":{
        (Line,):{
            args:("line",),
            trgt:Line.fromLine
        },
        ret:Line
    },
    "angle":{
        tuple():{
            args:tuple(),
            trgt:Line.angle
        },
        ret:float
    },
    "length":{
        tuple():{
            args:tuple(),
            trgt:Line.length
        },
        ret:float
    },
    "distanceFrom":{
        (Line,):{
            args:("obj",),
            trgt:Point.distanceTo
        },
        (Point,):{
            args:("obj",),
            trgt:Point.distanceTo
        },
        ret:float
    },
    "bisector":{
        tuple():{
            args:tuple(),
            trgt:Line.bisector
        },
        ret:Point
    },
    "sector":{
        (float, float,):{
            args:("m", "n",),
            trgt:Line.sector
        },
        ret:Point
    },
    "intersect":{
        (Line,):{
            args:("line",),
            trgt:Line.intersectionWith
        },
        ret:Point
    },
    "parallelLine":{
        (Point,):{
            args:("point",),
            trgt:Line.parallelLine
        },
        (float,):{
            args:("distance",),
            trgt:Line.parallelLine
        },
        ret:Point
    },
    "projectionOf":{
        (Point,):{
            args:("point",),
            trgt:Line.projectionOf
        },
        ret:Point
    },
    "perpendicularFrom":{
        (Point,):{
            args:("point",),
            trgt:Line.perpendicularFrom
        },
        ret:Line
    },
    "perpendicularAt":{
        (Point,):{
            args:("var",),
            trgt:Line.perpendicularAt
        },
        (float,):{
            args:("var",),
            trgt:Line.perpendicularAt
        },
        ret:Line
    },
    "perpendicularBisector":{
        tuple():{
            args:tuple(),
            trgt:Line.perpendicularBisector
        },
        ret:Line
    },
    "triangle":{
        (Point,):{
            args:("point",),
            trgt:Line.triangleTo
        },
        ret:Triangle
    },
    "circle":{
        tuple():{
            args:tuple(),
            trgt:Line.circleAround
        },
        ret:Circle
    },
    "tangentCircle":{
        (Point,):{
            args:("tangentPoint"),
            trgt:Line.circleAround
        },
        ret:Circle
    },
    "chordCircle":{
        (Point,):{
            args:("chordPoint"),
            trgt:Line.circleAround
        },
        ret:Circle
    },
    "quad":{
        (str,):{
            args:("direction"),
            trgt:Line.square
        },
        ret:pass
    },
    "rectangle":{
        (float, str,):{
            args:("sideLength", "direction"),
            trgt:Line.rectangle
        },
        ret:pass
    }
}