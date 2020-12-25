"""Module for Point."""
from Drawables.Drawable import Drawable
from Drawables.Quad import Quadrilateral
from Drawables.Parallelogram import Parallelogram
from math import degrees, pi, radians
import numpy as np

class Rectangle(Parallelogram):
    """Base class of Parallelogram."""

    _square:str = "square"
    def __init__(self):
        """Class constructor."""
        super().__init__()

    @classmethod
    def fromPoints(cls, listOfPoint: list):
        """Build rectangle from provided points."""
        if len(listOfPoint) != 4:
            raise ValueError(
                "ValueError:\tThe Polygon can't even be "+
                "constructed as a quadrilateral."
            )
        new = Quadrilateral()
        new.setPolygon(listOfPoint)
        return cls.checkClass(new)

    @classmethod
    def fromLines(cls, listOfLine: list):
        """Build parallelogram from provided lines."""
        points = cls.edgeToVertex(listOfLine)
        return cls.fromPoints(points)

    @classmethod
    def fromRectangle(cls, rec):
        """Copy another parallelogram."""
        if isinstance(rec, cls):
            new = type(rec)()
            new.vertices = cls.newVertices(rec.vertices)
            new.size = rec.size
            new.clockwise = rec.clockwise
            return new
        raise TypeError(
            "TypeError:\tExpected Quadrilateral, "+
            f"received {type(rec).__name__}"
        )

    @classmethod
    def fromMetrics(cls, line=..., angleLine:float=..., lengthOther:float=...):
        """Draws a parallelogram from some metrics: a line(/line length), an internal angle, other length."""
        from Drawables.Line import Line
        from Drawables.Point import Point
        a,b=...,...
        if not isinstance(angleLine, (int, float)):
            angleLine = Drawable.randomAngleFull()
        if isinstance(line, Line):
            a, b = line.start, line.end
            angleLine = a.angleTo(b)
        else:
            a= Point.default()
            if isinstance(line, (float, int)):
                b = Point.fromMetrics(
                    angle=angleLine,
                    distance=line, point=a
                )
            else:
                line = Drawable.randomLength()
                b = Point.fromMetrics(
                    angle=angleLine, point=a,
                    distance=line
                )
        if not isinstance(lengthOther, (float, int)):
            lengthOther = Drawable.randomLength()
        angleLine += (pi * 0.5)
        d = Point.fromMetrics(angleLine, lengthOther, a)
        c = Point.fromMetrics(angleLine, lengthOther, b)
        return cls.fromPoints([a,b,c,d])

    @classmethod
    def default(cls, ):
        """Build a random Quadrilateral."""
        return cls.fromMetrics()


    # Helpers.
    @staticmethod
    def checkClass(trap:Quadrilateral):
        """Check if parallelogram can be constructed."""
        new = trap.checkSubClass()
        if isinstance(new, Rectangle):
            return new
        raise ValueError(
            "ValueError:\tThe Quadrilateral can't "+
            "be constructed as a parallelogram."
        )