k = 1; M = 3; s = 0

while k <= M:
    term = 1.0/k
    s += term
    k += 1
print 'The sum s equals %.3f' % s

'''
Unix> python compute_sum_while.py
The sum s equals 5.187
'''
