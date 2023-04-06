#Optimized Bubble Sort in Python
def bubble_sort(alist):
    """
    Bubble sort is a sorting algorithm that compares two adjacent elements and swaps 
    them until they are in the intended order.
    Time Complexity	:
    Best	            = O(n)
    Worst	            = O(n2)
    Average	            = O(n2)
    Space Complexity	= O(2)
    Stability	        = Yes
    """
    n = len(alist) - 1
    no_swap = True 
    counter = 0
    for x in range(n,0,-1):
        counter += 1 
        for y in range(0,x):
            # Compare second element with first element.
            if alist[y + 1] < alist[y]:
                print("Swap applied bwteen " + str(alist[y + 1]) + " and " + str(alist[y]))
                alist[y + 1], alist[y] = alist[y] , alist[y + 1]
                no_swap = False
        print("counter: "+ str(counter))
        if no_swap: # if no swap is applied then alist is already sorted
            return 
        


def insertion_sort(alist):
    """
    Insertion sort is a sorting algorithm that places an unsorted 
    element at its suitable place in each iteration.
    Time Complexity	:
    Best	            = O(n)
    Worst	            = O(n2)
    Average	            = O(n2)
    Space Complexity	= O(1)
    Stability	        = Yes
    """
    n = len(alist)
    assert len(alist) > 0, "A list cannot be empty"
    for x in range(1,n):
        temp = alist[x]
        # j pointer is use for backward check
        j = x - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


def selection_sort(alist):
    """
    Selection sort is a sorting algorithm that selects the smallest element from an unsorted list 
    in each iteration and places that element at the beginning of the unsorted list.
    Time Complexity	:
    Best	            = O(n2)
    Worst	            = O(n2)
    Average	            = O(n2)
    Space Complexity	= O(1)
    Stability	        = No
    """
    n = len(alist)
    
    for step in range(n):
        min_idx = step # first elem consider as min value
        for nxt in range(step + 1, n):
            if alist[min_idx] > alist[nxt]:
                min_idx = nxt # update the min index if next value is smaller then previous 
        # placed min at the correction position
        alist[min_idx], alist[step]= alist[step],alist[min_idx]



def merge_sort(alist):
    """
    Merge Sort is one of the most popular sorting algorithms that is based on the 
    principle of Divide and Conquer Algorithm.
    Time Complexity	:
    Best	            = O(n*logn)
    Worst	            = O(n*logn)
    Average	            = O(n*logn)
    Space Complexity	= O(n)
    Stability	        = Yes
    """
    if len(alist) > 1:
        mid = len(alist) //2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k  = 0 # Three pointer, i for left, j for right and k for alist

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        # check left subarray has element 
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        
        # check right subarray has element 
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1


def __partition(alist,low,high):

    # choose the rightmost elements as pivot
    pivot = alist[high]

    i = low - 1 # pointer for the greater element

    for idx in range(low,high):
        if alist[idx] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1
            # swap element at i with element at idx
            alist[idx],alist[i] = alist[i],alist[idx]

    # swap the pivot element with the greater element specified by i
    alist[i + 1],alist[high] = alist[high],alist[i + 1]

    return i + 1
            
             



def quick_sort(alist,low,high):
    """
    Quicksort is a sorting algorithm based on the divide and conquer approach where:
    1. An array is divided into subarrays by selecting a pivot element (element selected from the array).
       While dividing the array, the pivot element should be positioned in such a way that elements less 
       than pivot are kept on the left side and elements greater 
       than pivot are on the right side of the pivot.
    2.The left and right subarrays are also divided using the same approach. 
    This process continues until each subarray contains a single element.
    3.At this point, elements are already sorted. Finally, elements are combined to form a sorted array.
    Time Complexity	:
    Best	            = O(n*logn)
    Worst	            = O(n2)
    Average	            = O(n*logn)
    Space Complexity	= O(logn)
    Stability	        = No
    """
    if low < high:

        pi = __partition(alist,low,high)

        quick_sort(alist,low,pi -1)
        quick_sort(alist,pi + 1, high)


def counting_sort(alist):
    """
    Counting sort is a sorting algorithm that sorts the elements of an array by counting 
    the number of occurrences of each unique element in the array. The count is stored in an 
    auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.
    Time Complexity	:
    Best	            = O(n + k)
    Worst	            = O(n + k)
    Average	            = O(n + k)
    Space Complexity	= O(max)
    Stability	        = Yes
    """
    size = len(alist)
    output = [0] * size

    #Initialize count alist
    max_value = max(alist) + 1
    count = [0] * max_value
    print("count: ",count)
    #store the count of each element in count list
    for i in range(size):
        count[alist[i]] += 1
    print("cummulative count: ",count)
    #store the cummulative count
    for i in range(1,max_value):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[alist[i]] - 1] = alist[i]
        count[alist[i]] -= 1
        i -= 1
    
    # Copy the sorted elements into original array
    for i in range(size):
        alist[i] = output[i]


def __counting_sort(alist,place):
    size = len(alist)
    output = [0] * size
    count = [0] * 10

    #calculate the count of elements
    for i in range(size):
        index = alist[i] // place
        count[index %10] += 1

    #calculate the cummulative count
    for i in range(1,10):
        count[i] += count[i - 1]

    #place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = alist[i] // place
        output[count[index % 10 ] - 1] = alist[i]
        count[index % 10 ] -= 1
        i -= 1

    # copy the output element to original list
    for i in range(size):
        alist[i] = output[i]
        

def radix_sort(alist):
    """
    Radix sort is a sorting algorithm that sorts the elements by first grouping the individual digits 
    of the same place value. Then, sort the elements according to their increasing/decreasing order.
    Time Complexity	:
    Best	            = O(n + k)
    Worst	            = O(n + k)
    Average	            = O(n + k)
    Space Complexity	= O(max)
    Stability	        = Yes
    """
    #get maximun element
    max_elem = max(alist)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_elem // place > 0:
        __counting_sort(alist,place)
        place *= 10


def  bucket_sort(alist):
    """
    Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups 
    called buckets. Each bucket is then sorted by using any of the suitable sorting algorithms or 
    recursively applying the same bucket algorithm.
    Time Complexity	:
    Best	            = O(n + k)
    Worst	            = O(n2)
    Average	            = O(n)
    Space Complexity	= O(n + k)
    Stability	        = Yes
    """

    bucket = [ [] for _ in range(len(alist))]

    # Insert element into their respective bucket 
    for j in alist:
        index = int(10* j)
        bucket[index].append(j)

    #Sort the elements of each buckets
    for i in range(len(alist)):
        bucket[i] = sorted(bucket[i])
    
    # Get the sorted elements
    k = 0
    for i in range(len(alist)):
        for j in range(len(bucket[i])):
            alist[k] = bucket[i][j]
            k += 1
    return alist



def __heapify(arr,n,i):
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

        __heapify(arr,n,largest)
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
        __heapify(arr,n,i)

    print("arr: ",arr)
    for i in range(n - 1,0,-1):
        # Swap
        arr[i],arr[0] = arr[0],arr[i]
        # Heapify root element
        __heapify(arr,i,0)


def shell_sort(alist):
    """
    Shell sort is a generalized version of the insertion sort algorithm. 
    It first sorts elements that are far apart from each other and successively reduces the 
    interval between the elements to be sorted.

    The interval between the elements is reduced based on the sequence used. 
    Some of the optimal sequences that can be used in the shell sort algorithm are:

    Shell's original sequence: N/2 , N/4 , …, 1
    Knuth's increments: 1, 4, 13, …, (3k – 1) / 2
    Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
    Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…
    Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
    Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....
    Time Complexity	:
    Best	            = O(nlog n)
    Worst	            = O(n2)
    Average	            = O(nlog n)
    Space Complexity	= O(1)
    Stability	        = No
    """
    n = len(alist)
    interval = n // 2

    while interval > 0:
        for i in range(interval,n):
            temp = alist[i]
            j = i
            while j >= interval and alist[j - interval] > temp:
                alist[j] = alist[j - interval]
                j -= interval
            alist[j] = temp
        interval //=2


    






