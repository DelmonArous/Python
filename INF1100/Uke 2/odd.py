n = 1
N = 100
odd_list = []

while n <= N:
    odd = 2*n - 1
    n += 1
    odd_list.append(odd)
print odd_list

odd_list1 = [2*n-1 for n in range(1,N+1)]
print odd_list1
