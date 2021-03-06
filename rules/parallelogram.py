"""Point Structure."""
from rules.drawable import *
paralleloADT = {
    parent:(Trapezoid,),
    "new":{
        (list, Point,):{
            args:("listOfPoint",),
            trgt:Parallelogram.fromPoints,
        },
        (list, Line,):{
            args:("listOfLine",),
            trgt:Parallelogram.fromLines,
        },
        (Line, float, float):{
            args:("line", "angle", "length",),
            trgt:Parallelogram.fromMetrics,
        },
        (float, float, float, float):{
            args:("line", "angleLine", "angle", "length",),
            trgt:Parallelogram.fromMetrics,
        },
        (float, float, float):{
            args:("line", "angle", "length",),
            trgt:Parallelogram.fromMetrics,
        },
        tuple():{
            args:tuple(),
            trgt:Parallelogram.default
        },
        retVal:Parallelogram
    },
    "copy":{
        tuple():{
            args:tuple(),
            trgt:Parallelogram.fromParallelogram
        },
        retVal:Parallelogram
    }
}