from searching import linear_search

array = [2, 4, 0, 1, 9]
x = 1
result = linear_search(array, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)