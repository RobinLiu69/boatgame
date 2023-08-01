import math

def forceToVelocity(self1, F, d):
    xa = math.cos(math.radians(d))*F/self1.mass
    ya = math.sin(math.radians(d))*F/self1.mass
    return xa, ya

def xyVelocityToOneDerectionVelocity(xv, yv):
    V = (xv**2+yv**2)**0.5
    d = math.degrees(math.atan2(yv, xv))
    return V,d

def oneDerectionVelocityToxyVelocity(V, d):
    xv = math.cos(math.radians(d))*V
    yv = math.sin(math.radians(d))*V
    return xv, yv