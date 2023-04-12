#Optimized Bubble Sort in Python
def bubble_sort(alist):
    """
    Bubble sort is a sorting algorithm that compares two adjacent elements and swaps 
    them until they are in the intended order.
    Time Complexity	:
    Best	            = O(n)
    Worst	            = O(n2)
    Average	            = O(n2)
    Space Complexity	= O(2)
    Stability	        = Yes
    """
    n = len(alist) - 1
    no_swap = True 
    counter = 0
    for x in range(n,0,-1):
        counter += 1 
        for y in range(0,x):
            # Compare second element with first element.
            if alist[y + 1] < alist[y]:
                print("Swap applied bwteen " + str(alist[y + 1]) + " and " + str(alist[y]))
                alist[y + 1], alist[y] = alist[y] , alist[y + 1]
                no_swap = False
        print("counter: "+ str(counter))
        if no_swap: # if no swap is applied then alist is already sorted
            return 
        

a = [2,7,4,3,5,1,6]
bubble_sort(a)
print(a)

a = ["My","name","is","sumit","maurya"]
bubble_sort(a)
print(a)

#example
my_str = "My name is sumit maurya"
lst = [(x, len(x)) for x in my_str.split(" ")]
print(lst)
n = len(lst)-1
no_swap = True

for x in range(n,0,-1):
    for y in range(0,x):
        if lst[y + 1][1] <  lst[y][1]:
            lst[y + 1],lst[y] = lst[y],lst[y + 1]
            no_swap = False
        elif lst[y + 1][1] == lst[y][1] and lst[y + 1][0] > lst[y][0]:
            lst[y + 1],lst[y] = lst[y],lst[y + 1]
            no_swap = False
    if no_swap:
        break

print(lst)


