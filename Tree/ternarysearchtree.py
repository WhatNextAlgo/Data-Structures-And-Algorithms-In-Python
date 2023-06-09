class Node:
    def __init__(self,character):
        self.character = character
        self.left = None
        self.middle = None
        self.right = None
        self.leaf = False
        self.value = None
        


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def put(self,key,value):
        self.root = self.insert(self.root,key,value,0)

    
    def insert(self,node,key,value,index):
        c = key[index]

        if node is None:
            node = Node(c)
        if c < node.character:
            node.left = self.insert(node.left,key,value,index)
        elif c > node.character:
            node.right = self.insert(node.right,key,value,index)
        elif index < len(key) - 1:
            node.middle = self.insert(node.middle,key,value,index + 1)
        else:
            node.leaf = True
            node.value = value
        return node


    def get(self,key):
        node = self.retrieve(self.root,key,0)
        if node is None:
            return None
        return node.value
    
    def retrieve(self,node,key,index):
        if node is None:
            return None
        
        c = key[index]

        if c < node.character:
            return self.retrieve(node.left,key,index)
        elif c > node.character:
            return self.retrieve(node.right,key,index)
        elif index < len(key) -1:
            return self.retrieve(node.middle,key,index + 1)
        else:
            if not node.leaf:
                return None
            return node
    
    def traverse_tree(self,node,s):
        # if we hit a leaf node (or a node that contains value)
        if node.value is not None:
            print("%s : %s "%(s + node.character,node.value))
        if node.left is not None:
            self.traverse_tree(node.left,s)

        if node.middle is not None:
            self.traverse_tree(node.middle,s + node.character)

        if node.right is not None:
            self.traverse_tree(node.right,s)

        return s

    def traverse(self):
        if self.root is not None:
            self.traverse_tree(self.root,'')
        
        

if __name__ == "__main__":
    t = TernarySearchTree()
    t.put("apple",10)
    t.put("apar",22)
    t.put("aat",2)
    t.put("bus",7)
    t.put("cat",9)
    t.put("dog",50)

    print(t.get("approve"))
    print(t.get("bus"))
    print(t.get("cat"))
    t.traverse()
            