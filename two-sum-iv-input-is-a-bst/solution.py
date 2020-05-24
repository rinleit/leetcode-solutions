# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        maps = set()
        return self.find(root, k, maps)
        
    def find(self, root, k, maps):
        if not root: return False
        if k - root.val in maps: return True
        maps.add(root.val)
        return self.find(root.left, k, maps) or self.find(root.right, k, maps)