class Spring:
    def __init__(self, k):
        self.k = k
    
    def force(self, x):
        return self.k*x
    
    def energy(self, x):
        return 0.5*self.k*x**2

S = Spring(0.2)

def table(f, a, b, n):
    print ''
    h = (b-a)/float(n)
    for i in range(n+1):
        x = a + i*h
        print 'function value = %10.4f at x = %g' % (f(x), x)

table(S.force, 0, 20, 20)
print '-------------------'
table(S.energy, 0, 20, 20)

class Nonelinear_Spring:
    def __init__(self, f, k):
        self.f, self.k, self.a = f, k
        
    def force(self, x):
        f = self.f
        return f(x)

    def energy(self, x):
        a = 0
        f = self.f

        h = (x-a)/100.
        I = 0.5*f(a)
        for i in iseq(1, n-1):
            I += f(1 + i*h)
        I += 0.5*f(x)
        I *= h
        return I

N_S = Nonelinear_Spring(a*sin(x), 0.2)
N_S.force(x)
N_S.energy(x)
