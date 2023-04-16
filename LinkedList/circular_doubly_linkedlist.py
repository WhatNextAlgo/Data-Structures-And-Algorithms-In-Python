class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    
    def get_node(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr == self.head:
                return
        return curr
    
    def insert_after(self,ref_node,new_node):
        new_node.next = ref_node.next
        new_node.prev = ref_node
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_before(self,ref_node,new_node):
        self.insert_after(ref_node.prev,new_node)

    def insert_at_end(self,new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.head.prev,new_node)

    def insert_at_beg(self,new_node):
        self.insert_at_end(new_node)
        self.head = new_node


    def remove(self,node):
        if self.head.next == self.head and self.head == node:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.head == node:
                self.head = node.next

    def __str__(self):
        if self.head is None:return "[]"
        lst_repr = []
        curr = self.head
        while True:
            lst_repr.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        return "["+ "-> ".join(lst_repr) + "]"  
    

if __name__ == "__main__":
    cd = CircularDoublyLinkedList()

    for x in range(0,5):
        cd.insert_at_beg(Node(x))

    print("After insert at beg: ",cd)

    for x in range(5,11):
        cd.insert_at_end(Node(x))

    print("After insert at end: ",cd)

    cd.insert_after(cd.get_node(4),Node(11))
    print("Insert after node 0: ",cd)
    cd.insert_before(cd.get_node(4),Node(12))
    print("Insert before node 0: ",cd)

    print("removeing node")

    cd.remove(cd.get_node(4))
    print("after removing node 12: ",cd)
    cd.remove(cd.get_node(5))
    print("after removing node 11: ",cd)






