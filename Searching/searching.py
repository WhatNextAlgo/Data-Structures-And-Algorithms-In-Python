def linear_search(alist,elem):
    """
    Linear search is a sequential searching algorithm where we start from one end and 
    check every element of the list until the desired element is found. 
    It is the simplest searching algorithm.
    Time Complexity: O(n)
    """
    n = len(alist)
    for idx in range(n):
        if alist[idx] == elem:
            return idx
    else:
        return -1
    

def binary_search_iterative(alist,elem,low,high):
    """
    Binary Search is a searching algorithm for finding an element's position in a sorted array.
    In this approach, the element is always searched in the middle of a portion of an array.
    Time Complexities

    Best case complexity: O(1)
    Average case complexity: O(log n)
    Worst case complexity: O(log n)
    Space Complexity

    The space complexity of the binary search is O(1).
    """

    while low <= high:
        mid = low + (high - low)// 2
        if alist[mid] == elem:
            return mid
        elif alist[mid] < elem:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_rec(alist,elem,low,high):
    if high >= low:
        mid = low + (high - low)//2
        if alist[mid] == elem:
            return mid
        # Search the left half
        elif alist[mid] > elem:
            return binary_search_rec(alist,elem,low,mid - 1)
        # Search the right half
        else:
            return binary_search_rec(alist,elem,mid + 1, high)
    else:
        return -1

