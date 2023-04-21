ALPHABET_SIZE = 26

class Node:
    def __init__(self,character):
        # nodes are characters in a trie 
        self.character = character
        # every node may have serveral children - this is why tries are not memory-efficent
        # every node has 26 children no matter they are needed or not
        self.children = [None for _ in range(ALPHABET_SIZE)] 
        self.leaf = False


class Trie:
    def __init__(self):
        # the root node is empty node (here we use *)
        self.root = Node("*")

    def insert(self,word):
        # always start with root node
        current = self.root
        for char in word:
            # we are dealing with indexes: use ASCII representation to get the index and transform
            # with the range [0- ALPHABET_SIZE]
            ascii_index = ord(char) - ord('a')
            if current.children[ascii_index] is not None:
                # keep going with creating a node with the given character
                current = current.children[ascii_index]
            else:
                node = Node(char)
                current.children[ascii_index] = node
                current = node

        # after we considered all the letters of the word
        # then we set the leaf node to True. it means end of the word   
        current.leaf = True


    def find(self,word):
        # if the tree is empty then return False
        if not self.root.children:
            return False
        
        current = self.root
        # considered all the letters
        for char in word:
            ascii_index = ord(char) - ord('a')
            if current.children[ascii_index] is not None:
                current = current.children[ascii_index]
            else:
                # otherwise we know the word is not present
                return False
        #if we've considered all the letters and the actual node is a leaf node:
        # we found the word
        if current.leaf:
            return True
        
        return False
    
    def sort(self):
        return self.get_words_prefix("")
    
    def get_words_prefix(self,prefix):
        node = self.root
        # we store the words in a list
        words = []

        # we consider all the letters
        for char in prefix:
            ascii_index = ord(char) - ord('a')
            if node.children[ascii_index] is None:
                return None
            node = node.children[ascii_index]
        
        # then we collect the words startig with prefix
        self.collect(node,prefix,words)
        return words

    # depth first search start with the last node of the prefix
    def collect(self,node,prefix,words):
        # recursive base condition
        if node is None:
            return 
        
        if node.leaf:
            #node we keep appending letters to the prefix (so this prefix is
            # not the original prefix any more)
            words.append(prefix)
        for child in node.children:
            if not child:
                continue
            child_character = child.character
            self.collect(child,prefix+child_character,words)
        


    


if __name__ == "__main__":
    trie = Trie()
    trie.insert("sea")
    trie.insert("seashell")
    trie.insert("shell")
    trie.insert("computer")
    trie.insert("science")
    trie.insert("apple")
    print(trie.find("sea"))
    print(trie.find("car"))
    print(trie.find("science"))
    print(trie.find("computer"))

    print(trie.get_words_prefix("s"))
    print(trie.sort())

