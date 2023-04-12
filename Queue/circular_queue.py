#Implement CircularQueue Data Structures

class CircularQueue:
    def __init__(self,k):
        self.k = k
        self.head = self.tail = -1
        self.items = [None] * k

    # Insert an element into the circular queue
    def enqueue(self,value):
        if ((self.tail + 1 ) % self.k) == self.head:
            print("The circule queue is full\n")
        
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.items[self.tail] = value
        else:
            self.tail = (self.tail + 1) % self.k
            self.items[self.tail] = value
    
    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty")
            return None
        elif (self.head == self.tail):
            temp = self.items[self.head]
            self.items[self.head] = None
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.items[self.head]
            self.items[self.head] =  None
            self.head = (self.head + 1 % self.k)
            return temp
        
    
    def __str__(self):
        if self.head == -1:
            return "["+ ", ".join([ str(x) for x in self.items]) + "]"
        return "[" + ", ".join([ str(x) for x in self.items]) + "]"
    
if __name__ == "__main__":
    obj = CircularQueue(5)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    print("Initial queue")
    print(obj)

    obj.dequeue()
    print("After removing an element from the queue")
    print(obj)
    obj.enqueue(6)
    print("After adding an element in the queue")
    print(obj)  
        

            

    