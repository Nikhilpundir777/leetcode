# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # Locate the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # If the node to delete is found
            
            # Case 1: Node has no children or one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 2: Node has two children
            # Replace with the minimum value in the right subtree
            min_larger_node = self.findMin(root.right)
            root.val = min_larger_node.val
            root.right = self.deleteNode(root.right, min_larger_node.val)
        
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        # Find the leftmost node (smallest value) in the subtree
        while node.left:
            node = node.left
        return node