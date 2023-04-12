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

a = [2,7,4,3,5,1,6]
insertion_sort(a)
print(a)


a = ["My","name","is","sumit","maurya"]
insertion_sort(a)
print(a)