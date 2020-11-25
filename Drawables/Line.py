"""Module Line."""
from numpy.core.numeric import ComplexWarning
from Drawables.Drawable import Drawable
import numpy as np
from math import inf, pi, radians, degrees, atan, sin, sqrt, cos


class Line(Drawable):
    """Description of class."""

    __name__ = "Line"
    def __init__(self):
        """Construct default."""
        from Drawables.Point import Point
        super().__init__()
        # Drawable.__init__(self)
        self.start:Point
        self.end:Point

    @classmethod
    def fromLine(cls, line, distance:float=0):
        """Derive another line from an existing one."""
        from Drawables.Point import Point
        if not isinstance(line, cls):
            raise TypeError("Type mismatch")
        new = cls()
        angle = line.slope()
        angle = atan(angle) + (pi / 2)
        if line.start.Y > line.end.Y:
            distance *= -1
        new.start = Point.fromMetrics(angle, distance, line.start)
        new.end = Point.fromMetrics(angle, distance, line.end)
        return new

    @classmethod
    def fromPoints(cls, pointA, pointB):
        """Construct a line provided two end-points are given."""
        new = cls()
        new.start = pointA
        new.end = pointB
        return new

    @classmethod
    def fromMetrics(cls, angle:float, length:float, point):
        """Draw Line using some metrics."""
        from Drawables.Point import Point
        new = cls()
        new.start = point
        new.end = Point.fromMetrics(angle, length, point)
        return new

    def length(self):
        """Find length of the Line segment."""
        try:
            return self._length
        except(Exception):
            self._length = self.start.distanceTo(self.end)
            return(self._length)

    def lenghtl1(self):
        """Find length of the Line segment."""
        try:
            return self._length
        except(Exception):
            self._lengthL1 = self.start.distanceL1(self.end)
            return self.start.distanceL1(self.end)

    def slope(self):
        """Return slope of line."""
        return(self.start.slopeTo(self.end))

    def getMetrics(self):
        """Return slope and y-intercept of Line segment."""
        #y = mx + c
        m = self.slope()
        if m == inf:
            return(inf, self.start.X)
        (x, y) = self.start.getPoint()
        c = (y - m * x)
        return(m, c)

    def parallelLine(self, distance):
        new = Line.fromLine(self)
        """        if distance == 0:
            return new"""
        angle = atan(new.slope()) + (0.5 * pi)
        new._translate(distance * cos(angle), distance * sin(angle))
        return new

    def intersectionWith(self, line):
        from Drawables.Point import Point
        (m1, c1) = self.getMetrics()
        (m2, c2) = line.getMetrics()
        x = (c1 - c2) / (m2 - m1)
        y = m1 * x + c1
        return(Point.fromCoOrdinates(x, y))

    def bisector(self):
        from Drawables.Point import Point
        return(Point.middlePoint(self.start, self.end))
        #return self.sector(1)

    def distanceFromLine(self, line):
        (m1, c1) = self.getMetrics()
        (m2, c2) = line.getMetrics()
        print(m1, m2)
        if abs(m1 - m2) > self.comparisonLimit:
            return inf
        angle_rad = atan(abs(m1))
        return abs(c1 - c2) * cos(angle_rad)

    def sector(self, ratio:float):
        from Drawables.Point import Point
        m = ratio
        ratio = ratio + 1
        n = 1
        x = abs(n * self.start.X - m * self.end.X) / ratio
        y = abs(n * self.start.Y - m * self.end.Y) / ratio
        return(Point.fromCoOrdinates(x, y))

    def projectionOf(self, point):
        l  = self.start.distanceTo(self.end)
        l1 = self.start.distanceTo(point)
        l2 = self.end.distanceTo(point)
        n = ((l ** 2) + (l2 ** 2) - (l1 ** 2)) / (2 * l)
        m = l - n
        return self.sector(m/n)

    def distanceFromPoint(self, point):
        return point.distanceToPoint(self.projectionOf(point))

    def perpendicularTo(self, point):
        return Line.fromPoints(self.projectionOf(point), point)
        # x = (c1 - c2) / (m2 - m1)
        # y = m1 * x + c1
        # return(Point.fromCoOrdinates(x, y))

    def perpendicularAtRatio(self, ratio:float):
        return(self.perpendicularAtPoint(self.sector(ratio)))


    def perpendicularAtPoint(self, point):
        from Drawables.Point import Point
        len_ = self.length()
        angle = degrees(atan(self.slope()))
        point1 = Point.fromMetrics( angle, len_, point)
        point2 = Point.fromMetrics( angle, len_, point)
        return(Line.fromPoints(point1, point2))

    def perpendicularBisector(self):
        return(self.perpendicularAtPoint(self.bisector()))

    def triangleTo(self, point):
        from Drawables.Triangle import Triangle
        return Triangle.fromLine(self, point)

    def circleAround(self, distance:float=0, point=None):
        if point == None:
            mid = self.bisector()
            radius = self.length() / 2
            return mid.circleAroundRadius(radius)
        else:
            return(point.circleAroundChord(self, distance))

    def square(direction:int=1):
        pass

    def rectangle(sideLength:float, direction:int=1):
        pass

    def _scale(self, sx:float=1, sy:float=1):
        self.start._scale(sx, sy)
        self.end._scale(sx, sy)


    def _translate(self, tx:float=0, ty:float=0):
        self.start._translate(tx, ty)
        self.end._translate(tx, ty)

    def _rotate(self, centre=None,angle:float=0):
        from Drawables.Point import Point
        if not isinstance(centre, Point):
            centre = Point()
        self.start._rotate(centre, angle)
        self.end._rotate(centre, angle)

    def _reflectPoint(self, point):
        self.start._reflectPoint(point)
        self.end._reflectPoint(point)

    def _reflectLine(self, line):
        self.start._reflectLine(line)
        self.end._reflectLine(line)

    def __ne__(self, o) -> bool:
        """'!=' operator overload."""
        return not self == o

    def __eq__(self, o) -> bool:
        """'==' operator overload."""
        return(self.start == o.start and self.end == o.end)

    def __str__(self) -> str:
        """Text return."""
        return f"Points: ({self.start.X}, {self.start.Y}), ({self.end.X}, {self.end.Y})"

    def draw(self, axes):
        """Draw plots."""
        x = self.start.X, self.end.X
        y = self.start.Y, self.end.Y
        axes.plot(x,y)