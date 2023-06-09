class ZAlgorithm:
    def __init__(self,pattern,text):
        self.pattern = pattern
        self.text = text
        # we have to concatenate the pattern and text
        self.S = pattern + text
        # int table for z table
        self.Z = [0 for _ in range(len(self.S))]

    def construct_z_table(self):
        # the first item (index 0) is the length of the S
        self.Z[0] =  len(self.S)

        # the first and last items in the Z box
        left = 0
        right = 0

        # consider all the letters of the S string (starting with index 1)
        for k in range(1,len(self.S)):
            # we are not in with in a Z box( navie approach) CASE 1
            if k > right:
                n = 0

                while n + k < len(self.S) and self.S[n] == self.S[n + k]:
                    n = n + 1
                
                self.Z[k] = n

                if n > 0:
                    left = k
                    right = k + n - 1
            else:
                # we are inside a Z box so may be copy the value one by one
                p = k - left
                # case II when we can copy the value
                if self.Z[p] < right - k + 1:
                    self.Z[k] = self.Z[p]
                else:
                    # we can not copy the values (CASE III)
                    i = right + 1
                    while i < len(self.S) and self.S[i] == self.S[i - k]:
                        i = i + 1
                    self.Z[k] = i - k
                    left = k
                    right = i - 1


    
    def search(self):
        self.construct_z_table()
        print(self.Z)
        # we just have to consider the values in Z table in O(N + M)    
        for i in range(1,len(self.Z)):
            if self.Z[i] >= len(self.pattern):
                print("Match found the index %s "% (i -  len(self.pattern)))



if __name__ == "__main__":
    # algorithm = ZAlgorithm('test','this is a test')
    algorithm = ZAlgorithm('aabza', 'abzcaabzaabza')
    algorithm.search()

            

