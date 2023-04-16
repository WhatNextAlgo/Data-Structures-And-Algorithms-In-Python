class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # get node at particular index
    def get_node(self,index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return
            curr = curr.next
        return curr
    
    def insert_after(self,ref_node,new_node):
        new_node.prev = ref_node
        if ref_node.next is None:
            self.tail = new_node
        else:
            new_node.next = ref_node.next
            new_node.next.prev = new_node
        
        ref_node.next = new_node

    def insert_before(self,ref_node,new_node):
        new_node.next = ref_node
        if ref_node.prev is None:
            self.head = new_node
        else:
            new_node.prev = ref_node.prev
            ref_node.prev.next = new_node
        ref_node.prev = new_node 

    def insert_at_beg(self,new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.insert_before(self.head,new_node)

    def insert_at_end(self,new_node):
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.insert_after(self.tail,new_node)

    def remove(self,node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def __str__(self):
        if self.head is None:return "[]"
        curr = self.head
        lst_repr = []
        while curr:
            lst_repr.append(str(curr.data))
            curr = curr.next
        return "["+ "-> ".join(lst_repr) + "]" 
    

if __name__ == "__main__":
    d = DoublyLinkedList()

    for x in range(0,5):
        d.insert_at_beg(Node(x))

    print("After insert at beg: ",d)

    for x in range(5,11):
        d.insert_at_end(Node(x))

    print("After insert at end: ",d)

    d.insert_after(d.get_node(4),Node(11))
    print("Insert after node 0: ",d)
    d.insert_before(d.get_node(4),Node(12))
    print("Insert before node 0: ",d)

    print("removeing node")

    d.remove(d.get_node(4))
    print("after removing node 12: ",d)
    d.remove(d.get_node(5))
    print("after removing node 11: ",d)

