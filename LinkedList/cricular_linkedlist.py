class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def get_node(self,index):
        if self.head is None:
            return None
        curr = self.head
        # iterate until index
        for i in range(index):
            curr = curr.next
            # check if next is pointing to head
            if curr == self.head: 
                return None
        return curr
    
    def get_prev_node(self,ref_node):
        if self.head is None:
            return None
        curr = self.head
        while curr.next != ref_node:
            curr = curr.next
        return curr

    def insert_after(self,ref_node,node):
        node.next = ref_node.next
        ref_node.next = node
    
    def insert_before(self,ref_node,node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node,node)

    def insert_at_end(self,node):
        if self.head is None:
            self.head = node
            node.next = node
        else:
            self.insert_before(self.head,node)
    
    def insert_at_beg(self,node):
        self.insert_at_end(node)
        self.head = node

    def remove(self,node):
        if self.head is None:return None
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            prev_node = self.get_prev_node(node)

            prev_node.next = node.next
            if self.head == node:
                self.head = node.next
            node.next = None


    def __str__(self):
        if self.head is None:return "[]"
        curr = self.head
        lst_repr = []
        while True:
            lst_repr.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        return "["+ "-> ".join(lst_repr) + "]" 


if __name__ == "__main__":
    c = CircularLinkedList()
    for x in range(1,5):
        c.insert_at_beg(Node(x))
    print("After Insert at beg: ", c)

    c.insert_after(c.get_node(3),Node(0))

    print("After Insert after node 1: ", c)

    for x in range(5,11):
        c.insert_at_end(Node(x))

    print("After Insert at end: ", c)

    for _ in range(0,5):
        c.remove(c.get_node(0))
        
    print("After removing node 0 ", c)
