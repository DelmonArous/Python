p = 5
N = 4
n = 1
x_prev = 100

print 'n=0 : %g' % (x_prev)

while n <= N:
    x = x_prev + (p/100.)*x_prev
    x_prev = x
    print 'n=%d : %g' % (n, x)
    n += 1

'''
Unix> python growth_years_efficient.py
n=0 : 100
n=1 : 105
n=2 : 110.25
n=3 : 115.763
n=4 : 121.551
'''
