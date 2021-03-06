import __init__
from Drawables.Drawable import Drawable
import math
from Drawables.Point import Point
from Drawables.Line import  Line
drawables = []
p1 = Point.fromCoOrdinates(0,0)
drawables.append(p1)
p2 = Point.fromPoint(p1)
drawables.append(p2)
p2._translate(2,2)

p3 = Point.fromPoint(p1)

p3._translate(0,-2)
drawables.append(p3)

print(p1, "\n", p2, "\n", p3, "\n")
"""
print(p1.slopeTo(p2))
print(p1.angleTo(p2))
print(p2.angleTo(p1))
print()
"""
l1 = Line.fromPoints(p2,p3)
drawables.append(l1)
dist = p1.angleFromLine(l1)
print(l1)
print(math.degrees(dist),"\n")


print(p1.slopeTo(p3))
print(p3.slopeTo(p1))

p4 = Point.middlePoint(p1, p2)
print(p4)
drawables.append(p4)

a = p1.distanceSquared(p2)
b = p1.distanceTo(point=p2)
print(a,b)

Drawable.draw(drawables)