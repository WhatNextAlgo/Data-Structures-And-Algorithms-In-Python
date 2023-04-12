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
array = [2, 4, 0, 1, 9]
x = 1
result = linear_search(array, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)