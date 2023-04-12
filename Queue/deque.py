#Implement Dequeue Data structrue

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def add_front(self,value):
        self.items.insert(0,value)
    
    def add_rear(self,value):
        self.items.append(value)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
    
    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
    
    def __str__(self):
        if self.items != []:
            return "[" + ", ".join([str(elem) for elem in self.items]) +"]"
        return "[]"
    

if __name__ == "__main__":

    d = Deque()
    d.add_rear(1)
    d.add_rear(2)
    d.add_rear(3)
    d.add_front(4)
    d.add_front(5)
    print(d)
    print("front peek: ",d.peek_front())
    print("rear peek: ",d.peek_rear())
    d.remove_front()
    print(d)
    d.remove_front()
    print(d)


