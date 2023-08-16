class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            sum_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                sum_coeff[i] += other.coeff[i]
        else: 
            sum_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                sum_coeff[i] += self.coeff[i]
        return Polynomial(sum_coeff)

    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            sum_coeff = self.coeff[:]
            for i in range(len(other.coeff)):
                sum_coeff[i] -= other.coeff[i]
        else:
            sum_coeff = other.coeff[:]
            for i in range(len(self.coeff)):
                sum_coeff[i] -= self.coeff[i]
        return Polynomial(sum_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = zeros(M+N-1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)
