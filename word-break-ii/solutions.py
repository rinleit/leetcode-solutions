from collections import defaultdict, deque
from copy import deepcopy
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
    def find_all_paths(self, graph, start, end, path=[]):
        path += [start]
        if start == end: return [path]
        if start not in graph: return []
        paths = []
        for node in graph[start]:
            new_path = deepcopy(path)
            paths.extend(self.find_all_paths(graph, node, end, new_path))
        return paths
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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
        is_goal = False

        while stack:
            p = stack.pop()
            nodes = graph[p]
            for node in nodes:
                if node == goal:
                    is_goal = True
                    break
                if node not in visited:
                    visited.add(node)
                    stack.append(node)

        if not is_goal: return []
        paths = self.find_all_paths(graph, 0, goal)
        ans = []
        for path in paths:
            ss = ''
            for i in range(1, len(path)): 
                ss += s[path[i-1]:path[i]] + ' '
            ans += [ss.strip()]
        return ans