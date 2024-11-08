def insertion_sort_count_swaps(arr):
    n = 6
    swap_count = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1 
        arr[j + 1] = key
    
    return swap_count


input_data = '6 10 4 5 1 2'
arr =  list(map(int, input_data.split()))

result = insertion_sort_count_swaps(arr) 
print(result)