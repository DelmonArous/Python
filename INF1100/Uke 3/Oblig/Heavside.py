def H(x):
    
    if x < 0:
        return 0
    elif x >= 0:
        return 1

print 'H(%g) = %g' % (-0.5, H(-0.5))
print 'H(%g) = %g' % (0, H(0))
print 'H(%g) = %g' % (10, H(10))

'''
Unix> python Heavside.py
H(-0.5) = 0
H(0) = 1
H(10) = 1
'''
