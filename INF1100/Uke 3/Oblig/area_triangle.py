def area(vertices):
    
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]

    A = 0.5*((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))
    A = abs(A)

    print 'The area of the triangle is %.1f' % A

area([[0,0],[1,0],[0,2]])

'''
Unix> python area_triangle.py
The area of the triangle is 1.0
'''
