"""
A perfect binary tree is a type of binary tree in which every internal node 
has exactly two child nodes and all the leaf nodes are at the same level.
"""
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#calcuate the depth
def calculate_depth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d

def isperfect_binarytree(root,depth,level= 0):
    if root is None: return True

    if (root.left is None) and (root.right is None):
        return (depth == level + 1)
    
    if (root.left is None) or (root.right is None):
        return False
    
    return (isperfect_binarytree(root.left,depth,level + 1) and 
            isperfect_binarytree(root.right,depth,level + 1))

    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    if isperfect_binarytree(root,calculate_depth(root),0):
        print("The tree is perfect binary tree")
    else:
        print("The tree is not a perfect binary tree")