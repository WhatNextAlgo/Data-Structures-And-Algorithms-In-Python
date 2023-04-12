def counting_sort(alist,place):
    size = len(alist)
    output = [0] * size
    count = [0] * 10

    #calculate the count of elements
    for i in range(size):
        index = alist[i] // place
        count[index %10] += 1

    #calculate the cummulative count
    for i in range(1,10):
        count[i] += count[i - 1]

    #place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = alist[i] // place
        output[count[index % 10 ] - 1] = alist[i]
        count[index % 10 ] -= 1
        i -= 1

    # copy the output element to original list
    for i in range(size):
        alist[i] = output[i]
        

def radix_sort(alist):
    """
    Radix sort is a sorting algorithm that sorts the elements by first grouping the individual digits 
    of the same place value. Then, sort the elements according to their increasing/decreasing order.
    Time Complexity	:
    Best	            = O(n + k)
    Worst	            = O(n + k)
    Average	            = O(n + k)
    Space Complexity	= O(max)
    Stability	        = Yes
    """
    #get maximun element
    max_elem = max(alist)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_elem // place > 0:
        counting_sort(alist,place)
        place *= 10

data = [121, 432, 564, 23, 1, 45, 788]
radix_sort(data)
print(data)
print(radix_sort.__doc__)