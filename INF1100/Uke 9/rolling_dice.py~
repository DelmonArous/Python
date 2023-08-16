import random, sys

def die():
    return random.randint(1, 6)

def getting_1_6(N):
    six = 0
    for i in range(N):
        eyes = die()
        if eyes == 6:
            six += 1

    probability = float(six)/N
    return probability

def getting_4_6(N):
    M = 0
    for i in range(N):
        eyes = [die() for i in range(4)]
        success = [6 for j in range(4)]
        if eyes == success:
            M += 1
    return float(M)/N

def getting_1_6_after_3(N):
    M = 0
    N_3_6 = 0
    for i in range(N):
        if [die() for i in range(3)] == [6, 6, 6]:
            N_3_6 += 1
            eyes = die()
            if eyes == 6:
                M += 1
    return float(M)/N_3_6

N = int(sys.argv[1])
print 'Probability of getting a 6:', 1./6
print 'Probability of getting 4 6 in a row:', getting_4_6(N)
print 'Probability of getting a 6 after 3 6s:', getting_1_6_after_3(N)
