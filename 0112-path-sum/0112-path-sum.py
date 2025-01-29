# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Return False for an empty tree
        if not root:
            return False

        # Check if it's a leaf node and the targetSum matches
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursive call on left and right with updated targetSum
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        