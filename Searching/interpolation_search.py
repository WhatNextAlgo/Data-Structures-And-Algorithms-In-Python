from searching import interpolation_search

# Driver Code 
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, 
                22, 23, 24, 33, 35, 42, 47] 
n = len(arr)
  
x = 18 # Element to be searched 
index = interpolation_search(arr, n, x) 
  
if index != -1: 
    print("Element found at index",index)
else: 
    print("Element not found")