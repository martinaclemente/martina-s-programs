def merge_sorted_arrays(A, B):
    i, j = 0, 0
    C = []

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1

    while j < len(B):
        C.append(B[j])
        j += 1

    return ' '.join(map(str, C))

input_A = '2 4 10 18'
input_B = '-5 11 12'

A = list(map(int, input_A.split()))
B = list(map(int, input_B.split()))
print(merge_sorted_arrays(A, B))

