import random

def draw_ball(hat):
    color = random.choice(hat)
    hat.remove(color)
    return color, hat

def new_hat():
    colors = ('red', 'yellow', 'green', 'brown')
    hat = []
    for color in colors:
        for i in range(5):
            hat.append(color)
    return hat

def experiments(n, question, N):
    M = 0
    for k in range(N):
        hat = new_hat()
        balls = []
        for i in range(n):
            color, hat = draw_ball(hat)
            balls.append(color)
        if examine(question, balls):
            M += 1
    return float(M)/N

def examine(question, balls):
    if question == 1:
        return balls.count('red') >= 1 and balls.count('brown') == 1
    elif question == 2:
        return balls.count('red') == 1
    elif question == 3:
        return balls.count('red') == 2
    else:
        return balls.count('green') >= 3

N = int(raw_input('How many experiments? '))
question = int(raw_input('Question 1, 2, 3 or 4? '))

for n in [3, 5, 7, 10, 15]:
    p = experiments(n, question, N)
    print 'n = %2d, question %d, probability: %.3f' % (n, question, p)
