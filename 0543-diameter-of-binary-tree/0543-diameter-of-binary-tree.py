# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # To store the maximum diameter

        def dfs(node):
            if not node:
                return 0  # Base case: height of an empty subtree is 0
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the diameter (max path through the current node)
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1

        dfs(root)
        return self.diameter
     