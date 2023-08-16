import random, sys

N = int(sys.argv[1]) # number of experiments
n = int(sys.argv[2]) # n dice
nsix = 1             # Want at least one 6
M = 0                # number of successful events

for i in range(N):
    six = 0
    for j in range(n):
        r = random.randint(1, 6)
        if r == 6:
            six += 1
    if six >= nsix:
        M += 1

print '%d experiments: probability of getting at least one 6 with %d dice: %g %% ' \
    % (N, n, (float(M)/N)*100)

'''
Unix> python one6_2dice.py 100 2
100 experiments: probability of getting at least one 6 with 2 dice: 31 % 
'''
