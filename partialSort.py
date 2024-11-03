def k_smallest_elements(n, A, k):
    A.sort()
    return A[:k]

n = 10
input = '4 -6 7 8 -9 100 12 13 56 17'
A = list(map(int, input.split()))
k = 3

result = k_smallest_elements(n, A, k)
print(' '.join(map(str, result)))
