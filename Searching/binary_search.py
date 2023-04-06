from searching import binary_search_iterative,binary_search_rec

array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binary_search_iterative(array, x,0,len(array) - 1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


result = binary_search_rec(array, 7,0,len(array) -1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


