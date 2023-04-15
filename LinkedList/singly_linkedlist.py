class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # representation of single linked list
    def __str__(self):
        curr = self.head
        lst_repr = []
        while curr:
            lst_repr.append(str(curr.data))
            curr = curr.next
        return "["+ "-> ".join(lst_repr) + "]" if lst_repr != [] else "[]"
    

    def append(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def prepend(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node

    def insert_after(self,prev,data):
        if not prev:
            print("The given previous node must present in Singly Linked List")
            return
        node = Node(data)
        node.next = prev.next
        prev.next = node

    def delete(self,key):
        curr = self.head
        if curr is None:return
        # if head is a key
        if curr and curr.data == key:
            if curr.next is not None:
                self.head = curr.next
                curr = None
            else:
                self.head = curr.next
                self.tail = self.head
                curr = None

        # if head is not the key to delete
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is not None:
            if curr.next is None:
                prev.next = curr.next
                curr = None
                self.tail = prev
            else:
                prev.next = curr.next
                curr = None

    def delete_at_index(self,index):
        curr = self.head
        if curr is None:return
        # if index at 0 
        if index == 0: 
            if curr.next is not None:
                self.head = curr.next
                curr = None
            else:
                self.head = curr.next
                self.tail = self.head
                curr = None
        pos = 0 
        prev = None
        while curr and pos != index:
            pos += 1
            prev = curr
            curr = curr.next
        
        if curr is not None:
            if curr.next is None:
                prev.next = curr.next
                curr = None
                self.tail = prev
            else:
                prev.next = curr.next
                curr = None





        


if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(1,10):
        l.append(i)
    
    print("after append: ",l)

    for i in range(20,9,-1):
        l.prepend(i)

    print("after prepend: ",l)

    for i in range(20,0,-3):
        print(i,end = " ")
        l.delete(i)
    
    print("\n after deleting: ",l)
    
    print("before deleting at index: ",l)
    for i in range(4,10):
        l.delete_at_index(i)
        print(f"after deleting at index : {i} ",l)
    

        