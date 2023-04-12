import math
def jump_search(alist,value,n):
    """
    Just like Binary Search, Jump Search is one of the searching algorithms for sorted arrays. 
    The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps 
    or skipping some elements in place of searching all elements.

    Important points:

    1. Works only with sorted arrays.
    2. The optimal size of a block to be jumped is (√ n). This makes the time complexity of Jump Search O(√ n).
    3. The time complexity of Jump Search is between Linear Search ( ( O(n) ) and Binary Search ( O (Log n) ).
    Binary Search is better than Jump Search, but Jump search has an advantage that we traverse back only 
    once (Binary Search may require up to O(Log n) jumps, consider a situation where the element 
    to be search is the smallest element or smaller than the smallest). 
    So in a systems where jumping back is costly, we use Jump Search.
    Time Complexity : O(√n)
    Auxiliary Space : O(1)
    """

    # Find the block size to be jumped
    step = math.sqrt(n)

    # Finding the block where element is present (if it is present)
    prev = 0
    while alist[int(min(step,n)) -1] < value:
        prev = step
        step += math.sqrt(n)
        # if we exceed the list or reach to end of the list
        if prev >= n:
            return -1
        
    # Doing the linear search for value in block beginning with prev
    while alist[int(prev)] < value:
        prev += 1

        # If we reached next block or end  
        # of list, element is not present.
        if prev == min(step,n):
            return -1
    # If element is found
    if alist[int(prev)] == value:
        return prev
    return -1

# Driver code to test function 
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 89
n = len(arr) 
  
# Find the index of 'x' using Jump Search 
index = jump_search(arr, x, n) 
  
# Print the index where 'x' is located 
print("Number" , x, "is at index" ,"%.0f"%index)