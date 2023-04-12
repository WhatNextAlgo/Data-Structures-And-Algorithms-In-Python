def partition(alist,low,high):

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

        pi = partition(alist,low,high)

        quick_sort(alist,low,pi -1)
        quick_sort(alist,pi + 1, high)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)