# Pyhton program to implement binary heap
"""
Problem Solution
1. Create a class BinaryHeap with an instance variable items set to an empty list. This empty list is used to store the binary heap.
2. Define methods size, parent, left, right, get, get_max, extract_max, max_heapify, swap and insert.
3. The method size returns the number of elements in the heap.
4. The method parent takes an index as argument and returns the index of the parent.
5. The method left takes an index as argument and returns the index of its left child.
6. The method right takes an index as argument and returns the index of its right child.
7. The method get takes an index as argument and returns the key at the index.
8. The method get_max returns the maximum element in the heap by returning the first element in the list items.
9. The method extract_max returns the the maximum element in the heap and removes it.
10. The method max_heapify takes an index as argument and modifies the heap structure at and below the node at this index to make it satisfy the heap property.
11. The method swap takes two indexes as arguments and swaps the corresponding elements in the heap.
12. The method insert takes a key as argument and adds that key to the heap.

"""

class BinaryHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def parent(self,index):
        return (index - 1) // 2

    def left(self,index):
        return (2 * index) + 1 
    
    def right(self,index):
        return (2 * index) + 2
    
    def get(self,index):
        try:
            return self.items[index]
        except:
            return None
        
    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]
    
    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.items[0]
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest
    
    def max_heapify(self,index):
        largest = index
        l = self.left(index)
        r = self.right(index)

        if l <= self.size() -1 and self.items[l] > self.items[largest]:
            largest = l
        
        if r <= self.size() -1 and self.items[r] > self.items[largest]:
            largest = r

        if largest != index:
            self.swap(largest,index)
            self.max_heapify(largest)

        
    def swap(self,largest,index):
        self.items[index],self.items[largest] = self.items[largest],self.items[index]


    def insert(self,key):
        index = self.size()
        self.items.append(key)

        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p,index)
            index = p

    def __str__(self):
        if self.size() == 0: return '[]'
        return "[" + ", ".join([str(x) for x in self.items]) + "]"

if __name__ == "__main__":
    bheap = BinaryHeap()
    for i in range(1,10,2):
        bheap.insert(i)

    for i in range(20,10,-2):
        bheap.insert(i)

    print(bheap.get_max())
    print(bheap)
    print(bheap.extract_max())
    print(bheap)
    print(bheap.get_max())

