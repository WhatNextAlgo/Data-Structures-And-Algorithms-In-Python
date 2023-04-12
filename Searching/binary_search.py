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
    
    
array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search_iterative(array, x,0,len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


result = binary_search_rec(array, 7,0,len(array) -1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


