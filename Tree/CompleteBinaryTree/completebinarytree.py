"""
A complete binary tree is a binary tree in which all the levels are completely filled 
except possibly the lowest one, which is filled from the left.

A complete binary tree is just like a full binary tree, but with two major differences:

1. All the leaf elements must lean towards the left.
2. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't 
have to be a full binary tree.
"""
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def count_node(node):
    if node is None:return 0
    return 1 + count_node(node.left) + count_node(node.right)

def iscomplete_binarytree(root,index,num_of_node):
    if root is None:return True
    if index >= num_of_node: return False

    return (iscomplete_binarytree(root.left,2 * index + 1,num_of_node) and
            iscomplete_binarytree(root.right,2 * index + 2,num_of_node))

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    num_of_node = count_node(root)
    index = 0
    if iscomplete_binarytree(root,index,num_of_node):
        print("The tree is complete binary tree")
    else:
        print("The tree is not a complete binary tree")
    