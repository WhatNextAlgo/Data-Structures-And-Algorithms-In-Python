#Implement Queue Data Structures

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items  == []
    
    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    
    def __str__(self):
        if self.items != []:
            return "[" + ", ".join([str(elem) for elem in self.items]) +"]"
        return "[]"
    

if __name__  == "__main__":
    q = Queue()
    q.enqueue(1)
    print(q)
    print("dequeue: ",q.dequeue())
    q.enqueue(2)
    print("peek: ",q.peek())
    q.enqueue(3)
    q.enqueue(4)
    print(q)