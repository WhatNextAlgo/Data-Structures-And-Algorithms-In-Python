from sorting import quick_sort
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)