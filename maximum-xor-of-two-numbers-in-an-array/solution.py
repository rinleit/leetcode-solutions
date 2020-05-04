class Trie:
    def __init__(self):
        self.root = dict()
    
    def build(self, arr):
        for n in arr:
            self.add(n)

    def add(self, number):
        word = "{:032b}".format(number)
        curr = self.root
        for c in word:
            c = int(c)
            if c not in curr:
                curr[c] = dict()
            curr = curr[c]
        curr['*'] = True
    
    def find_best_number_to_xor(self, number):
        word = "{:032b}".format(number)
        curr = self.root
        best_number = ''
        for c in word:
            c = int(c)
            xor = c ^ 1
            c = xor if xor in curr else c
            curr = curr[c]
            best_number += str(c)
        return int(best_number, 2)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        trie.build(nums)
        max_xor = 0
        for n in nums:
            max_xor = max(max_xor, n ^ trie.find_best_number_to_xor(n))
        return max_xor
        
        