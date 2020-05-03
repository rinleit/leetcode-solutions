from collections import defaultdict, deque

class Trie:
    def __init__(self):
        self.root = dict()
    
    def build(self, arr):
        for word in arr: self.add(word)

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = dict()
            curr = curr[c]
        curr['*'] = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        trie.build(wordDict)
        n = len(s)
        graph = defaultdict(set)
        latest = deque([0])
        checked = set()
        while latest:
            start = latest.pop()
            if start in checked: continue
            checked.add(start)
            curr = trie.root
            i = start
            while i < n:
                if s[i] in curr:
                    curr = curr[s[i]]
                    if '*' in curr:
                        graph[start].add(i+1)
                        latest.append(i+1)
                else:
                    break
                i += 1
        
        goal = n
        stack = deque([0])
        visited = set([0])

        while stack:
            p = stack.pop()
            nodes = graph[p]
            for node in nodes:
                if node == goal:
                    return True
                if node not in visited:
                    visited.add(node)
                    stack.append(node)
        return False
