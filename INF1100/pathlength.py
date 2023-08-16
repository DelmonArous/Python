from math import *

def pathlength(x,y):

    n = 100

    for i in range(1, n - 1):
        xi = x + i
        yi = y + i
        L = sqrt((xi - (xi - 1))**(2) + (yi - (yi - 1))**(2))
    return L
    
