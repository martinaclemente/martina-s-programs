def partition_array(A):
    pivot = A[0]  
    left_part = []
    right_part = []

    for x in A[1:]:
        if x <= pivot:
            left_part.append(x)
        else:
            right_part.append(x)

    return left_part + [pivot] + right_part

n = 9
input = '7 2 5 6 1 3 9 4 8'
A = list(map(int, input.split()))

result = partition_array(A)
print(" ".join(map(str, result)))