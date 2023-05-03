class BinomialTree:
    def __init__(self,key):
        self.key = key
        self.children = []
        self.order = 0

    def add(self, node):
        self.children.append(node)
        self.order += 1


class BinomialHeap:
    def __init__(self):
        self.trees = []

    def extract_min(self):
        if self.trees == []:return None

        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
        return smallest_node

    def get_min(self):
        if self.trees == []:return None

        least = self.items[0]
        for tree in self.trees:
            if tree.key < least.key:
                least = tree.key
        return least
    
    def combine_roots(self,h):
        self.trees.extend(h.trees)
        self.trees.sort(key = lambda tree:tree.order)

    
    def merge(self,h):
        self.combine_roots(h)
        if self.trees == []:return None
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < i < len(self.trees) - 1 and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add(after_after)
                        del self.items[i + 2]
                    else:
                        after_after.add(after)
                        del self.trees[i + 1]

                else:
                    if current.key < after.key:
                        current.add(after)
                        del self.trees[i + 1]
                    else:
                        after.add(current)
                        del self.trees[i]
            i = i + 1

    def insert(self,key):
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)

    def dfs(self,tree,level):
        if tree.children == []:
            return
        for child in tree.children:
            print(level * " - " + str(child.key))
            if child.children != []:
                self.dfs(child,level + 1)

    def print_tree(self):
        for tree in self.trees:
            print(tree.key)
            self.dfs(tree,level = 1)

    def __str__(self):
        if self.trees == []: return "[]"
        self.print_tree()
        return ""

            


if __name__ == "__main__":
    bheap = BinomialHeap()

    bheap.insert(3)
    bheap.insert(7)
    bheap.insert(1)
    bheap.insert(4)
    bheap.insert(2)
    bheap.insert(5)
    print("Print before extract:")
    print(bheap)
    print("Min extract value: ",bheap.extract_min().key)
    print("Print after extract:")
    print(bheap)
    print("Min extract value: ",bheap.extract_min().key)
    print("Print after extract:")
    print(bheap)



