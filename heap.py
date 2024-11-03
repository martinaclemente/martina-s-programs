def heapify(arr, n, i): 
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l 
  
    if r < n and arr[r] > arr[largest]:
        largest = r
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def buildHeap(arr, n): 
    startIdx = n // 2 - 1 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)

n = 5
input= '1 3 5 7 2'
arr = list(map(int, input.split()))

buildHeap(arr, n)
print(" ".join(map(str, arr)))