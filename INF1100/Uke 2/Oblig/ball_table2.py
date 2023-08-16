v0 = 5; g = 9.81

t_list = [0.1*i for i in range(1,7,1)]
y_list = [v0*t-0.5*g*t**2 for t in t_list]

print ' t         y(t)'

for i in range(len(t_list)):
    print '%.2f s %7.3f m' % (t_list[i],y_list[i])

'''
Unix> python ball_table2.py
 t         y
0.10 s   0.451 m
0.20 s   0.804 m
0.30 s   1.059 m
0.40 s   1.215 m
0.50 s   1.274 m
0.60 s   1.234 m
'''
    
