import random

def draw_ball(hat):
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

def new_hat():
    colors = ('red', 'blue', 'yellow', 'purpule')
    hat = []
    for color in colors:
        for i in range(10):
            hat.append(color)
    return hat

n = 10
N = int(raw_input('How many experiments? '))
M = 0

for k in range(N):
    hat = new_hat()
    balls = []
    for i in range(n):
        color, hat = draw_ball(hat)
        balls.append(color)
    if balls.count('blue') and balls.count('purpule') == 2:
        M += 1

print 'Probability: ', float(M)/N
