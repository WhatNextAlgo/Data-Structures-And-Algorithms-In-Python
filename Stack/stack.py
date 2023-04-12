#Implement Stack Data Structures

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self,value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
        
    def __str__(self):
        if self.items != []:
            return "[" + ", ".join([str(elem) for elem in self.items]) +"]"
        return "[]"


if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    print("pop: ",s.pop())
    s.push(3)
    print("top: ",s.peek())
    print(s)