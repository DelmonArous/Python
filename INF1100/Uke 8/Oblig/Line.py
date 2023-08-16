class Line:
    def __init__(self, p1, p2):  #Two points p1(x0,y0) and p2(x1,y1)
        self.x0, self.y0 = p1
        self.x1, self.y1 = p2
        
    def value(self, x):
        a = (self.y1 - self.y0)/float(self.x1 - self.x0)  # slope
        b = self.y0 - a*self.x0 
        return a*x + b

line = Line((0,-1), (2,4))
print line.value(0.5), line.value(0), line.value(1)

'''
Unix> python Line.py
0.25 -1.0 1.5
'''
