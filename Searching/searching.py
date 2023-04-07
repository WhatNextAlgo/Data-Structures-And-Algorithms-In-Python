import math


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



def fibonaccian_search(arr,x,n):
    """
    Fibonacci search technique is a method of searching algorithms where a sorted array uses a 
    divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers.
    Compared to binary search where the sorted array is divided into two equal-sized parts, 
    one of which is examined further, Fibonacci search divides the array into two parts that 
    have sizes that are consecutive Fibonacci numbers.
    """
    # Initialize fibonacci numbers  
    fibMMm2 = 0 # (m-2)'th Fibonacci No. 
    fibMMm1 = 1 # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1 # m'th Fibonacci 
  
    # fibM is going to store the smallest  
    # Fibonacci Number greater than or equal to n  
    while (fibM < n): 
        fibMMm2 = fibMMm1 
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1 
  
    # Marks the eliminated range from front 
    offset = -1; 
  
    # while there are elements to be inspected. 
    # Note that we compare arr[fibMm2] with x. 
    # When fibM becomes 1, fibMm2 becomes 0  
    while (fibM > 1): 
          
        # Check if fibMm2 is a valid location 
        i = min(offset+fibMMm2, n-1) 
  
        # If x is greater than the value at  
        # index fibMm2, cut the subarray array  
        # from offset to i  
        if (arr[i] < x): 
            fibM = fibMMm1 
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            offset = i 
  
        # If x is greater than the value at  
        # index fibMm2, cut the subarray  
        # after i+1 
        elif (arr[i] > x): 
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2 
            fibMMm2 = fibM - fibMMm1 
  
        # element found. return index  
        else : 
            return i 
  
    # comparing the last element with x */ 
    if(fibMMm1 and arr[offset+1] == x): 
        return offset+1; 
  
    # element not found. return -1  
    return -1

