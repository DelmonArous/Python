from math import *

class Rectangle:
    def __init__(self, W, H, corner):
        self.x0, self.y0 = corner[0], corner[1]
        self.W, self.H = W, H

    def area(self):
        return self.W*self.H

    def circumference(self):
        return 2*self.W+2*self.H

class Triangle:
    def __init__(self, p1, p2, p3):
        self.x0, self.y0 = p1[0], p1[1]
        self.x1, self.y1 = p2[0], p2[1]
        self.x2, self.y2 = p3[0], p3[1]

    def area(self):
        x0, y0 = self.x0, self.y0
        x1, y1 = self.x1, self.y1
        x2, y2 = self.x2, self.y2
        return 0.5*((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))

    def distance(self):
        distance1 = sqrt((self.x1-self.x0)**2 + (self.y1-self.y0)**2))
        distance2 = sqrt((self.x2-self.x0)**2 + (self.y2-self.y0)**2))
        distance3 = sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2))

    def circumference(self):
        return distance1 + distance2 + distance3
