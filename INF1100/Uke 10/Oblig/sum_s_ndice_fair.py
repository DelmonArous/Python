import random, sys

try:
    N = int(sys.argv[1])   # number of experiments
    n = int(sys.argv[2])   # number of dice
    s = float(sys.argv[3]) # upper bound for sum of eyes
    q = float(sys.argv[4]) # cost is q units
except IndexError:
    print 'You have failed to provide cml arguments!'
    sys.exit(1)

unit = q  # All in!          
M = 0     # number of successful events

# computes the sum of eyes for n dice
def sum_of_eyes(n):
    return sum([random.randint(1, 6) for i in range(n)])

for k in range(N):
    if sum_of_eyes(n) < s: 
        M += 1

p = float(M)/N  # probability of winning
r = q/p         # fair payment

for i in range(N):    
    unit -= q     # subtract q units of money for each game    
    sum_eyes = sum_of_eyes(n)
    if sum_eyes < s:      
        unit += r # each win add r units of money

print '%d experiments: probability of winning throwing %d dice: %g %% ' \
    % (N, n, p*100)
print 'Average payment: %.2f, got %.2f units of money' % (r, unit)

'''
Unix> python sum_s_ndice_fair.py 10000 4 9 1
10000 experiments: probability of winning throwing 4 dice: 5.47 % 
Average payment: 18.28, got 403.19 units of money
'''
