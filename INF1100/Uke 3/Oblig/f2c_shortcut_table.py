Fdegrees = range(0,101,10)

C = [(F - 30)/2.0 for F in Fdegrees]
C_exact = [(5.0/9)*(F - 32) for F in Fdegrees]

table = [Fdegrees, C_exact, C]

print '     F       C       Approx. of C'

for i in range(len(Fdegrees)):
    print '%5d F %7.1f C  %10.1f C' % (table[0][i],table[1][i],table[2][i])

'''
Unix> python f2c_shortcut_table.py
     F       C       Approx. of C
    0 F   -17.8 C       -15.0 C
   10 F   -12.2 C       -10.0 C
   20 F    -6.7 C        -5.0 C
   30 F    -1.1 C         0.0 C
   40 F     4.4 C         5.0 C
   50 F    10.0 C        10.0 C
   60 F    15.6 C        15.0 C
   70 F    21.1 C        20.0 C
   80 F    26.7 C        25.0 C
   90 F    32.2 C        30.0 C
  100 F    37.8 C        35.0 C
'''
