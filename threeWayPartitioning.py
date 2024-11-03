def rearrange_array(n, A):
    pivot = A[0] 
    less_than = []  
    equal_to = []   
    greater_than = []  

    
    for num in A:
        if num < pivot:
            less_than.append(num)
        elif num == pivot:
            equal_to.append(num)
        else:
            greater_than.append(num)

    result = less_than + equal_to + greater_than
    return result

n = 9
input = '4 5 6 4 1 2 5 7 4'
A = list(map(int, input.split()))
B = rearrange_array(n, A)

print(" ".join(map(str, B)))
