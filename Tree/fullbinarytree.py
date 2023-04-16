"""
A full Binary tree is a special type of binary tree in which every parent node/internal node 
has either two or no children.
"""
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def isfull_binarytree(root):
    if root is None:return True

    # Checking whether child is present
    if root.left is None and root.right is None:
        return True
    if root.left and root.right:
        return isfull_binarytree(root.left) and isfull_binarytree(root.right)
    
    return False
    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.right.right = Node(6)

    if isfull_binarytree(root):
        print("The tree is full binary tree")
    else:
        print("The tree is not a full binary tree")