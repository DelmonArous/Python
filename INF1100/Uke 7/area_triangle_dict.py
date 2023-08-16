def area(vertices):
    
    x1, y1 = vertices[1]
    x2, y2 = vertices[2]
    x3, y3 = vertices[3]

    A = 0.5*((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(x2*y1))
    A = abs(A)

    return 'The area of the triangle is %.1f' % A

print area({1: (0,0),2: (1,0),3: (0,2)})

