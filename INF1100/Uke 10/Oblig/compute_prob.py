import random

M = 0      # Number of successful events

for i in [1, 2, 3, 6]: 
    N = 10**i
    for j in range(N):
        r = random.random()       # Generate a random number in the half open interval [0,1)
        if r > 0.5 and r < 0.6:   # Check if the number generated lies in the interval (0.5,0.6)
            M += 1
    print 'N = %g: probability: %g %% ' % (N, (float(M)/N)*100)


'''
Unix> python compute_prob.py
N = 10: probability: 10 % 
N = 100: probability: 11 % 
N = 1000: probability: 12.2 % 
N = 1e+06: probability: 10.0417 % 
'''
