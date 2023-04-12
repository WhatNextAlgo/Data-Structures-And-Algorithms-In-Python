def  bucket_sort(alist):
    """
    Bucket Sort is a sorting algorithm that divides the unsorted array elements into several groups 
    called buckets. Each bucket is then sorted by using any of the suitable sorting algorithms or 
    recursively applying the same bucket algorithm.
    Time Complexity	:
    Best	            = O(n + k)
    Worst	            = O(n2)
    Average	            = O(n)
    Space Complexity	= O(n + k)
    Stability	        = Yes
    """

    bucket = [ [] for _ in range(len(alist))]

    # Insert element into their respective bucket 
    for j in alist:
        index = int(10* j)
        bucket[index].append(j)

    #Sort the elements of each buckets
    for i in range(len(alist)):
        bucket[i] = sorted(bucket[i])
    
    # Get the sorted elements
    k = 0
    for i in range(len(alist)):
        for j in range(len(bucket[i])):
            alist[k] = bucket[i][j]
            k += 1
    return alist

array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucket_sort(array))
print(bucket_sort.__doc__)