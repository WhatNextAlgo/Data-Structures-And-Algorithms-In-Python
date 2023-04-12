def counting_sort(alist):
    """
    Counting sort is a sorting algorithm that sorts the elements of an array by counting 
    the number of occurrences of each unique element in the array. The count is stored in an 
    auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.
    Time Complexity	:
    Best	            = O(n + k)
    Worst	            = O(n + k)
    Average	            = O(n + k)
    Space Complexity	= O(max)
    Stability	        = Yes
    """
    size = len(alist)
    output = [0] * size

    #Initialize count alist
    max_value = max(alist) + 1
    count = [0] * max_value
    print("count: ",count)
    #store the count of each element in count list
    for i in range(size):
        count[alist[i]] += 1
    print("cummulative count: ",count)
    #store the cummulative count
    for i in range(1,max_value):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[alist[i]] - 1] = alist[i]
        count[alist[i]] -= 1
        i -= 1
    
    # Copy the sorted elements into original array
    for i in range(size):
        alist[i] = output[i]

data = [4, 2, 2, 8, 3, 3, 1]
counting_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)


data = [4, 2, 2, 8, 3, 23, 1]
counting_sort(data)
print("Sorted Array in Ascending Order: ")
print(data)