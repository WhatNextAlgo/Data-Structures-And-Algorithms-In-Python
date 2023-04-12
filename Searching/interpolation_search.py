def interpolation_search(alist,n,value):
    """
    Interpolation search is an improved variant of binary search. This search algorithm works on 
    the probing position of the required value. It was first described by W. W. Peterson in 1957.
    For this algorithm to work properly, the data collection should be in a 
    sorted form and equally distributed.
    Interpolation search is that type of searching algorithms, used for searching for a key in 
    an array that has been ordered by numerical values assigned to the keys ( key values ).
    Time Complexity: If elements are uniformly distributed, then O (log log n)). 
    In worst case it can take upto O(n).
    Auxiliary Space: O(1)
    """
    # Find the indexs of two corners
    low =0
    high = n -1 
    # Since array is sorted, an element present in array must be in range defined by corner
    while low <= high and value >= alist[low] and value <= alist[high]:
        if low == high:
            if alist[low] == value:
                return low
            return -1
        # Probing the position with keeping uniform distribution in mind.
        pos = low + int(((float(high - low) / (alist[high] - alist[low])) * (value - alist[low])))
        print("pos: ",pos)

        # Condition of target found 
        if alist[pos] == value:
            return pos
        
        # if value is larger, value is in upper part
        if alist[pos] < value:
            low = pos + 1
        # If x is smaller, x is in lower part 
        else:
            high = pos - 1

    return -1

# Driver Code 
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, 
                22, 23, 24, 33, 35, 42, 47] 
n = len(arr)
  
x = 18 # Element to be searched 
index = interpolation_search(arr, n, x) 
  
if index != -1: 
    print("Element found at index",index)
else: 
    print("Element not found")