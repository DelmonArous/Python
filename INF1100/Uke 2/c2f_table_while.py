Fdegrees = range(0,101,10)
print '     F       C'

for F in Fdegrees:
    C = (5*F - 160) / 9.
    print '%5d F %10.1f C' % (F, C)
    

