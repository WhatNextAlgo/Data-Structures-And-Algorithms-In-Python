def shell_sort(alist):
    """
    Shell sort is a generalized version of the insertion sort algorithm. 
    It first sorts elements that are far apart from each other and successively reduces the 
    interval between the elements to be sorted.

    The interval between the elements is reduced based on the sequence used. 
    Some of the optimal sequences that can be used in the shell sort algorithm are:

    Shell's original sequence: N/2 , N/4 , …, 1
    Knuth's increments: 1, 4, 13, …, (3k – 1) / 2
    Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1
    Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…
    Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...
    Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....
    Time Complexity	:
    Best	            = O(nlog n)
    Worst	            = O(n2)
    Average	            = O(nlog n)
    Space Complexity	= O(1)
    Stability	        = No
    """
    n = len(alist)
    interval = n // 2

    while interval > 0:
        for i in range(interval,n):
            temp = alist[i]
            j = i
            while j >= interval and alist[j - interval] > temp:
                alist[j] = alist[j - interval]
                j -= interval
            alist[j] = temp
        interval //=2


data = [9, 8, 3, 7, 5, 6, 4, 1]
shell_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
