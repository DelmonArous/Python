import random 

N = 10
head = 0

for i in range(N):
    r = random.random()
    if r <= 0.5:
        print 'head'
        head += 1
    else:
        print 'tail'

    # r = random.randint(1,2)
    # if r == 1: ...

coin = ['head', 'tail']
for i in range(N):
    r = random.choice(coin)
    if r == 'head':
        head += 1

print 'Got head %d times out of %d trials' % (head, N)
