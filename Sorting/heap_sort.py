def heapify(arr,n,i):
    # find the largest among root and children
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    #  If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest],arr[i] 

        heapify(arr,n,largest)

def heap_sort(arr):
    """
    Heap Sort is a popular and efficient sorting algorithm in computer programming. 
    Learning how to write the heap sort algorithm requires knowledge of 
    two types of data structures - arrays and trees.
    Time Complexity	:
    Best	            = O(nlog n)
    Worst	            = O(nlog n)
    Average	            = O(nlog n)
    Space Complexity	= O(1)
    Stability	        = No
    """
    n = len(arr)
    # Build max heap
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    print("arr: ",arr)
    for i in range(n - 1,0,-1):
        # Swap
        arr[i],arr[0] = arr[0],arr[i]
        # Heapify root element
        heapify(arr,i,0)

arr = [1, 12, 9, 5, 6, 10]
heap_sort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')