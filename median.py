def find_kth_smallest(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

n = 11
input = '2 36 5 21 8 13 11 20 5 4 1'
k = 8
A = list(map(int, input.split()))

result = find_kth_smallest(A, k)
print(result)