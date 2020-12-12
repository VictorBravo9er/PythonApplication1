"""Base class."""
import numpy as np
from math import sin, cos, inf, atan
import matplotlib.pyplot as plt
from numpy.core.arrayprint import printoptions
from numpy.lib.function_base import iterable

class Drawable(object):
    """Description of class."""

    @staticmethod
    def orientation(pointA, pointB, target):
        """Orientation test. 0 - go for it, 1 - decide, -1 - no go, next please. O(1)."""
        if target in (pointA, pointB):
            return -1
        buf = np.array([1, pointA.X, pointA.Y, 1, pointB.X, pointB.Y, 1, target.X, target.Y]).reshape(3,-1)
        buf = np.linalg.det(buf)
        if buf < 0:
            return -1
        if buf == 0:
            return 0
        return 1

    comparisonLimit = 0.00000001
    def __init__(self):
        """Build Base constructor."""
        object.__init__(self)
        # super().__init__()

    def rotateMatrix(self, rotation:float=0):
        """Rotate Matrix."""
        s = sin(rotation)
        c = cos(rotation)
        rotMat = self.getIdentityMatrix()
        rotMat[0][0] = c
        rotMat[0][1] = -s
        rotMat[1][0] = s
        rotMat[1][1] = c
        return rotMat

    def translateMatrix(self, tx:float=0, ty:float=0):
        """Translate Matrix."""
        trMat = self.getIdentityMatrix()
        trMat[0][2] = tx
        trMat[1][2] = ty
        return trMat

    def scaleMatrix(self, sx:float=1, sy:float=1):
        """Scale Matrix."""
        scMat = self.getIdentityMatrix()
        scMat[0][0] = sx
        scMat[1][1] = sy
        return scMat

    def shearMatrix(self, shx:float=0,shy:float=0):
        """Shear Matrix."""
        shMat = self.getIdentityMatrix()
        shMat[0][1] = shx
        shMat[1][0] = shy
        return shMat

    def reftectionMatrix(self, slope:float=0, intercept:float=0):
        """Reflect Matrix. Takes in slope and intercept."""
        trans, trans_ = None, None
        if slope == inf:
            trans = (-intercept, 0)
            trans_ = (intercept, 0)
        else:
            trans = (0, -intercept)
            trans_ = (0, intercept)
        refMat = self.translateMatrix(*trans)
        slope = atan(slope)
        refMat = np.dot(self.rotateMatrix(-slope), refMat)
        refMat = np.dot(self.scaleMatrix(1, -1), refMat)
        refMat = np.dot(self.rotateMatrix(slope), refMat)
        refMat = np.dot(self.translateMatrix(*trans_), refMat)
        """if slope == inf:
            refMat[0][0] = -1
        else:
            refMat[1][1] = -1
            if slope != 0:
                refMat[1][1] = -1
                theta = atan(slope)
                refMat = np.dot(self.rotateMatrix(theta), refMat)
                refMat = np.dot(refMat, self.rotateMatrix(-theta))
        if intercept == 0:
            return refMat
        elif slope ==inf:
            refMat = np.dot(self.translateMatrix(intercept), refMat)
            refMat = np.dot(refMat, self.translateMatrix(-intercept))
        else:
            refMat = np.dot(self.translateMatrix(0, intercept), refMat)
            refMat = np.dot(refMat, self.translateMatrix(0, -intercept))"""
        
        return refMat

    def getIdentityMatrix(self):
        """Identity Matrix."""
        return np.identity(3, dtype="float")

    @staticmethod
    def processData(data:tuple):
        try:
            msg, value = data
        except Exception as e:
            raise Exception(f"Expected 2 items, got {len(data)} items")
        print(f"{msg}\nValue{value}")

    @staticmethod
    def draw(drawables:list, num:str=""):
        """Draw call."""
        fig, ax = plt.subplots(1)
        ax.set_aspect(1)
        for drawable in drawables:
            t = type(drawable)
            if issubclass(t, Drawable):
                drawable.draw(ax)
            elif t == tuple:
                # process values other than drawable figures
                try:
                    Drawable.processData(drawable)
                except Exception as e:
                    print(e.args[0])
            else:
                print("Error with object:",drawable)
        fig.savefig(f"data/save{num}.png")
        plt.close()
        


    def __str__(self):
        """Text maker."""
        return super().__str__()
