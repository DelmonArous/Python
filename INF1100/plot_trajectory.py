from scitools.std import *

g = 9.81

try:
    y0 = float(sys.argv[1])
    degrees = float(sys.argv[2])
    v0 = float(sys.argv[3])
except IndexError:
    v0 = eval(raw_input('v0? '))
    degrees = eval(raw_input('degrees? '))
    y0 = eval(raw_input('y0? '))

def f(x):
    return x*tan(theta) - g*x**2/(2*v0**2)*1/(cos(theta))**2 + y0

def quadratic_roots(a, b, c):
    delta = b**2 - 4*a*c
    x1 = (-b + sqrt(delta))/(2*a)
    x2 = (-b - sqrt(delta))/(2*a)
    return x1, x2

theta = degrees*pi/180
a = -g/(2*v0)*1/(cos(theta))**2
b = tan(theta)
c = y0

x1_root, x2_root = quadratic_roots(a,b,c)
xmax = max(x1_root,x2_root)
x = linspace(0,xmax,201)

ymax = max(f(x))
maxaxis = max(ymax,xmax)

plot(x,f(x), axis=[0,maxaxis,0,maxaxis])
