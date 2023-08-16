from scitools.std import *

x0 = 100
p = 5
N = 4
index_set = range(N+1)
x = zeros(N+1)

x[0] = x0
for i in index_set[:-1]:
    print i
    x[i+1] = x[i] + (p/100.)*x[i]
print x
plot(index_set, x, 'ro', 
     xlabel='years',ylabel='amount')
