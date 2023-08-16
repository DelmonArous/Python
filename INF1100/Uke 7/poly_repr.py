list_pol = [0]*101
list_pol[0] = -0.5
list_pol[100] = 2.
dict_pol = {0: -0.5, 100: 2.}

def list(x):
    p = 0.
    for i in range(len(list_pol)):
        p += list_pol[i]*x**i
    return p

def dict(x):
    p = 0.
    for key in dict_pol:
        p += dict_pol[key]*x**key
    return p

print list(1.05)
print dict(1.05)
