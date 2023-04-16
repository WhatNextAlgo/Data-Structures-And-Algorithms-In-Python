class BinaryTree:
    def __init__(self,key = None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self,key):
        self.key = key

    def insert_left(self,new_node):
        self.left = new_node

    def insert_right(self,new_node):
        self.right = new_node

    def search(self,key):
        if self.key == key:
            return self
        if self.left is not None:
            temp = self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp = self.right.search(key)
            return temp
        return None
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key,end ="-> ")

        if self.right is not None:
            self.right.inorder()


if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.insert_left(BinaryTree(2))
    bt.insert_right(BinaryTree(3))
    left_node = bt.search(2)
    left_node.insert_left(BinaryTree(4))
    left_node.insert_right(BinaryTree(5))
    bt.inorder()

