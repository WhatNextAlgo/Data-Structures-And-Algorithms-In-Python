#Fenwick Tree also called as Binary indexed tree
class FenwickTree:
    def __init__(self,nums):
        # original array of numbers (integers)
        self.nums =nums
        # To constructed fenwick tree first item in array should start with 0.
        self.fenwick_tree = [0 for _ in range(len(nums) + 1)]


    # The sum of numbers in the interval [start:end]
    # O(log N) running time complexity
    def range_sum(self,start,end):
        return self.sum(end) - self.sum(start - 1)
    
    def sum(self,index):

        # indexes start with 0 but in the theory/implementation we start with 1
        index = index + 1
        total = 0

        while index > 0:
            total = total + self.fenwick_tree[index]
            index = self.parent(index)
        return total


    # construct the fenwick tree from the original array 
    # O(log N) running time complexity
    def construct(self):

        for index in range(1, len(self.nums) + 1):
            self.update(index,self.nums[index - 1])

    # O(logn) running time complexity
    def update(self,index, num):
        # have to check all the ranges that include the index
        while index < len(self.nums) + 1:
            self.fenwick_tree[index] += num
            # index of the next items
            index = self.next(index)

    # to calculate the next item
    # O(1) running time complexity
    def next(self,index):
        return index + (index&-index)
    
    # to calculate the parent item
    # O(1) running time complexity
    def parent(Self,index):
        return index - (index&-index)
    
    def __str__(self):
        if self.fenwick_tree != []:
            return "[" + ", ".join([str(x) for x in self.fenwick_tree]) + "]"
    

if __name__ == "__main__":
    nums = [3,2,-1,6,5,4,-3,3,7,2,3]

    tree = FenwickTree(nums)
    print("Before construct fenwick tree: ")
    print(tree)

    tree.construct()
    
    print("After construct fenwick tree: ")
    print(tree)

    print(tree.range_sum(2,5))
    print()
    
    

    

