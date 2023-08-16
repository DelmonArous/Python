from math import *

class Point:
    def __init__(self, x, y):
        self.x , self.y = x, y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

class PolarPoint(Point):
    def __init__(self, r, theta):
        self.r, self.theta = r, theta
        Point.__init__(self, self.r*cos(self.theta), self.r*sin(self.theta))

    def __str__(self):
        return 'Polar: (%g, %g)\nKartesisk: %s' \
            % (self.r, self.theta, Point.__str__(self))

a = PolarPoint(2, pi/3)
print a

