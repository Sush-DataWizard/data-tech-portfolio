
class TreeNode:
    def __init__(self,val,left=None, right=None):
        self.val = val
        self.left=left
        self.right=right

class Solution:
    def minDepth(self, A):
        if not A:
            return 0
        
        if not A.left:
            return 1 + self.minDepth(A.right)
        if not A.right:
            return 1 + self.minDepth(A.left)
        
        return 1 + min(self.minDepth(A.left),self.minDepth(A.right))