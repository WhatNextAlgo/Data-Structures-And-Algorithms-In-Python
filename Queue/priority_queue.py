# Implement Priority Queue (Max Heap)

class MaxHeap():

    def __init__(self,lst= []):
        if lst == []:
            self.lst = []
        else:
            self.lst = lst
            for i in range(self.size() // 2 - 1,-1,-1):
                self.heapify(i) 

    def size(self):
        return len(self.lst)
 
    def heapify(self,index):
        largest = index
        n = self.size()
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self.lst[left] > self.lst[index]:
            largest = left
        
        if right < n and self.lst[right] > self.lst[largest]:
            largest = right

        if largest != index:
            self.lst[index],self.lst[largest] = self.lst[largest],self.lst[index]
            self.heapify(largest)

    
    def insert(self,value):
        n = self.size()
        if n == 0:
            self.lst.append(value)
        else:
            self.lst.append(value)
            for i in range(self.size() // 2 - 1,-1,-1):
                self.heapify(i)

    def delete(self,value):
        n = self.size()
        i = 0
        for i in range(0,n):
            if value == self.lst[i]:
                break
        self.lst[i], self.lst[-1] = self.lst[-1], self.lst[i]
        del self.lst[-1]
        for i in range(self.size() // 2 -1,-1,-1):
            self.heapify(i)
    
    def __str__(self):
        if self.lst != []:
            return "[" + ", ".join([str(elem) for elem in self.lst]) +"]"
        return "[]"


if __name__ == "__main__":
    h = MaxHeap()
    h1 = MaxHeap([3,4,9,5,2])
    h.insert(3)
    h.insert(4)
    h.insert(9)
    h.insert(5)
    h.insert(2)

    print ("Max-Heap array: " + str(h)+ "\n" + str(h1))

    h.delete(4)
    h1.delete(4)
    print("After deleting an element: " + str(h) + "\n" + str(h1))
    h.delete(3)
    h1.delete(3)
    print("After deleting an element: " + str(h) + "\n" + str(h1))
    h.delete(9)
    h1.delete(9)
    print("After deleting an element: " + str(h) + "\n" + str(h1))

