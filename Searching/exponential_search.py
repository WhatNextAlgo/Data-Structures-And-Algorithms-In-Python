def __exp_bin_search(alist,low,high,value):
    if high >= low:
        mid = int(low + (high - low) / 2)
        # If the element is present at  
        # the middle itself 
        if alist[mid] == value: 
            return mid 
          
        # If the element is smaller than mid,  
        # then it can only be present in the  
        # left subarray 
        if alist[mid] > value: 
            return __exp_bin_search(alist, low, mid - 1, value) 
          
        # Else he element can only be 
        # present in the right 
        return __exp_bin_search(alist, mid + 1,high, value) 
    return -1

def exponential_search(alist,n,value):
    """
    Exponential search is also known as doubling or galloping search. 
    This mechanism is used to find the range where the search key may present.
    
    If L and U are the upper and lower bound of the list, then L and U both are the power of 2. 
    For the last section, the U is the last position of the list. For that reason, 
    it is known as exponential.
    After finding the specific range, it uses the binary search technique to find 
    the exact location of the search key.
    The name of this searching algorithm may be misleading as it works in O(Log n) time. 
    The name comes from the way it searches an element.
    """
    #If value is present at first position itself
    if alist[0] == value:
        return 0
    
    # Find range for binary search i by repeated doubling
    i = 1
    while i < n and alist[i] <= value:
        i = i * 2

    # call the binary search for the found range
    return __exp_bin_search(alist,i / 2, min(i,n), value) 

# Driver Code 
arr = [2, 3, 4, 10, 40] 
n = len(arr) 
x = 4
result = exponential_search(arr, n, x) 
if result == -1: 
    print("Element not found in the array")
else: 
    print("Element is present at index %d" %(result))
    