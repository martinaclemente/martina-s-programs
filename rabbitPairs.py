def rabbit_pairs(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    sequence = [0] * (n + 1)
    sequence[1] = 1
    sequence[2] = 1
    
    for i in range(3, n + 1):
        sequence[i] = sequence[i - 1] + k * sequence[i - 2]
    
    return sequence[n]

n = 5
k = 3
print(rabbit_pairs(n, k))  