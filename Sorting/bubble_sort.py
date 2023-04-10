from sorting import bubble_sort

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


