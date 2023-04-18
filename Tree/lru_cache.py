CAPACITY = 4
# Doubly Linked List Node
class Node:
    def __init__(self,id,data):
        self.id = id
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    # update the first and last items in O(1)
    def __init__(self):
        self.head = None
        self.tail = None


class LRUCache:
    def __init__(self):
        self.actual_size = 0
        # we can store id - Node pairs: this  is how we can find a node in O(1)
        self.dictionary = {}
        self.linked_list = DoublyLinkedList()

    # data can be website or anything
    def put(self,id,data):
        if id in self.dictionary:
            node = self.dictionary[id]
            node.data = data
            # update the node to head node (cache feature)
            self.update(node)
            return
        # if data is not present in the cache so insert
        node = Node(id,data)

        # we have to insert into the cache + set it to the head node
        if self.actual_size < CAPACITY:
            self.actual_size += 1
            self.add(node)

        else:
            self.remove_tail()
            self.add(node)

    # add node to the head of the doubly linked list
    def add(self,node):
        node.next = self.linked_list.head
        # node.prev = None

        # we have to update the previous head: point to the new head(which is the node)
        if self.linked_list.head:
            self.linked_list.head.prev = node

        # update the head node
        self.linked_list.head = node

        # if there is 1 node in the list: it is the head as well as the tail
        if not self.linked_list.tail:
            self.linked_list.tail = node

        # we have to update the dictionary with node
        self.dictionary[node.id] = node

    # remove last item (least frequently used)
    def remove_tail(self):
        # get the node from dictionary
        last_node = self.dictionary[self.linked_list.tail.id]

        # remove the node from dictionary
        del self.dictionary[self.linked_list.tail.id]
        # new tail node is the prev node (because we remove the actual one)
        self.linked_list.tail = self.linked_list.tail.prev
        if self.linked_list.tail:
            self.linked_list.tail.next = None
        
        last_node = None


    def get(self,id):
        # dictionary does not contain the item [O(1) running time]
        if id not in self.dictionary:
            return None
        node = self.dictionary[id]

        # move to the head (frequently visited items must be close to the head)
        self.update(node)
        return node
    
    # move the given node to the front
    def update(self,node):
        # from doubly linked list: we can get the previous and next node
        prev_node = node.prev
        next_node = node.next

        # so it is middle node (not the head) in the list
        if prev_node:
            prev_node.next = next_node
        else: # we know that this is the head (first node)
            self.linked_list.head = next_node

        # so the last node
        if next_node:
            next_node.prev = prev_node
        else: # we know it is the last node
            self.linked_list.tail =prev_node

        # we have to move the node to the first
        self.add(node)

    def __str__(self):
        actual_node = self.linked_list.head
        lst_repr = []
        while actual_node:
            lst_repr.append(str(actual_node.data))
            actual_node = actual_node.next
        return "[" + ", ".join(lst_repr) + "]"
        


if __name__ == "__main__":
    cache = LRUCache()
    cache.put(0,"www.google.com")
    cache.put(1,"www.facebook.com")
    cache.put(2,"www.twitter.com")
    cache.put(3,"www.whatnextalgo.github.io/leetcode")
    cache.put(4,"www.linkedin.com")

    print(cache)
    print(cache.get(3).data)
    print(cache)

    cache.put(5,"www.udemy.com")
    print(cache)



    
