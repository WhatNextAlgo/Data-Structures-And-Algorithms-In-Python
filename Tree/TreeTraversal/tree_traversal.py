from typing import Optional


class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root:Optional[Node]):
    if root:
        inorder(root.left)
        print(str(root.key),end="-> ")
        inorder(root.right)


def preorder(root:Optional[Node]):
    if root:
        print(str(root.key),end="-> ")
        preorder(root.left)
        preorder(root.right)

def postorder(root:Optional[Node]):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key),end="-> ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left= Node(4)
    root.left.right = Node(5)

    print("InOrder Traversal: ")
    inorder(root)
    print("\nPreOrder Traversal: ")
    preorder(root)
    print("\nPostOrder Traversal: ")
    postorder(root)

