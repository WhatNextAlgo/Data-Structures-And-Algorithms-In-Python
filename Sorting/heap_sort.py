from sorting import heap_sort

arr = [1, 12, 9, 5, 6, 10]
heap_sort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')