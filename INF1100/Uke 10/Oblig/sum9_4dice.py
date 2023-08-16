import random, sys

N = int(sys.argv[1]) # number of experiments
ndice = 4            # number of dice
unit = 1             # start out with 1 unit of money 
M = 0                # number of successful events

for i in range(N):
    s = 0            # sum of eyes
    unit -= 1        # for each experiment we pay 1 unit of money
    for j in range(ndice):
        r = random.randint(1, 6)
        s += r
    if s < 9:        # if the sum of eyes is less than 9
        unit += 10   # you win 10 units of money
        M += 1       # this is counted as an successful event

print '%d experiments: probability of winning: %g %% ' \
    % (N, (float(M)/N)*100)
print 'You got %g units of money' % unit

'''
Unix> python sum9_4dice.py 10000
10000 experiments: probability of winning: 5.45 % 
You got -4549 units of money
'''
