from searching import exponential_search
# Driver Code 
arr = [2, 3, 4, 10, 40] 
n = len(arr) 
x = 4
result = exponential_search(arr, n, x) 
if result == -1: 
    print("Element not found in the array")
else: 
    print("Element is present at index %d" %(result))
    