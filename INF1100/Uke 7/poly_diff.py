def diff(x):
    
    dp = {}  
    for j in x:
        if j != 0:
            dp[j-1] = j*x[j]
    return dp

p = {0: -3, 3: 2, 5: 1}
print diff(p)

        
