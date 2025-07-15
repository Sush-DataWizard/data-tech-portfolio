class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base cases
        if not p and not q:     # Both are None
            return True
        if not p or not q:      # One is None, other not
            return False
        if p.val != q.val:      # Values differ
            return False
        
        # Recursively check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
