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

a = [2,7,4,3,5,1,6]
selection_sort(a)
print(a)

a = ["My","name","is","sumit","maurya"]
selection_sort(a)
print(a)


