list = []
h = 0.01

# x1 = [1 + i*h for i in range(1,101,1)]

for i in range(0,101,1):
    xi = 1 + i*h
    list.append(xi)

print list
