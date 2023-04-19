class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent= parent
        self.left = None
        self.right = None
        

class SplayTree:
    def __init__(self):
        self.root = None

    
    # it is exactly the same as BST
    def insert(self,data):
        if self.root is None:
            self.root = Node(data,None)
        else:
            self.insert_node(data,self.root)

    #BST Insertion
    def insert_node(self,data,node):
        if data < node.data:
            if node.left:
                self.insert_node(data,node.left)
            else:
                node.left = Node(data,node)
        else:
            if node.right:
                self.insert_node(data,node.right)
            else:
                node.right = Node(data,node)


    # find a given arbitary item in the BST
    def find(self,data):
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                self.splay(node)
                return node.data
            
    def splay(self,node):

        # until we hit the root node. we have to iterate.
        while node.parent is not None:
            # the node is a left or right child of the root node
            # zig situation
            if node.parent.parent is None:
                if node == node.parent.left:
                    self.rotate_right(node.parent)
                else:
                    self.rotate_left(node.parent)
            # zig zig situation
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                self.rotate_right(node.parent.parent)
                self.rotate_right(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                self.rotate_left(node.parent.parent)
                self.rotate_left(node.parent)
            
            #zig-zag situation
            elif node == node.parent.left and node.parent == node.parent.parent.right:
                self.rotate_right(node.parent)
                self.rotate_left(node.parent)
            else:
                self.rotate_left(node.parent)
                self.rotate_right(node.parent)
            
    
    def rotate_right(self,node):
        temp_left_node = node.left
        t = temp_left_node.right

        temp_left_node.right = node
        node.left = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left == node:
            temp_left_node.parent.left = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right == node:
            temp_left_node.parent.right = temp_left_node

        
        if node == self.root:
            self.root = temp_left_node


    def rotate_left(self,node):
        temp_right_node = node.right
        t = temp_right_node.left

        temp_right_node.left = node
        node.right = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left == node:
            temp_right_node.parent.left = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right == node:
            temp_right_node.parent.right = temp_right_node

        
        if node == self.root:
            self.root = temp_right_node


if __name__ == '__main__':

    splay_tree = SplayTree()
    splay_tree.insert(10)
    splay_tree.insert(8)
    splay_tree.insert(3)
    splay_tree.insert(7)
    print(splay_tree.root.data)
    splay_tree.find(7)
    print(splay_tree.root.data)
    splay_tree.find(3)
    print(splay_tree.root.data)
    splay_tree.find(8)
    print(splay_tree.root.data)
    splay_tree.find(3)
    print(splay_tree.root.data)



