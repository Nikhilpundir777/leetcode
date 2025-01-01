# # Definition for singly-linked list.
# class ListNode:
#      def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head  # Fast pointer
        tortoise = head  # Slow pointer
        
        while hare and hare.next:
            hare = hare.next.next  # Hare moves two steps
            tortoise = tortoise.next  # Tortoise moves one step
            
            if hare == tortoise:  # If they meet, there is a cycle
                return True
        
        return False  # If loop exits, no cycle