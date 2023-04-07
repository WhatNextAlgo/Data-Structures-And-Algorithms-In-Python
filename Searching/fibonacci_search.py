from searching import fibonaccian_search

# Driver Code 
arr = [10, 22, 35, 40, 45, 50, 
       80, 82, 85, 90, 100] 
n = len(arr) 
x = 85
print("Found at index:", fibonaccian_search(arr, x, n))