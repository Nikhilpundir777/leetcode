# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function to perform inorder traversal
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Perform inorder traversal and get the kth element
        return inorder(root)[k - 1]