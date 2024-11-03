def quick_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = 7
input = '5 -2 4 7 8 -10 11'
A = list(map(int, input.split()))

quick_sort(A)
print(" ".join(map(str, A)))