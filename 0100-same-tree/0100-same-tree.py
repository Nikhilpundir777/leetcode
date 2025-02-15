# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
         # Base case: both trees are empty, they are the same
        if not p and not q:
            return True
        
        # If one of them is empty and the other is not, they are not the same
        if not p or not q:
            return False
        
        # If the values of the current nodes are different, trees are not the same
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)