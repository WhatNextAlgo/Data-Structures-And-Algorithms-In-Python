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

a = [2,7,4,3,5,1,6]
merge_sort(a)
print(a)

a = ["My","name","is","sumit","maurya"]
merge_sort(a)
print(a)