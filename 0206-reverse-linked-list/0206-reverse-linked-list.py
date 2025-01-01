# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initially, there is no previous node
        curr = head  # Start with the head of the list
        
        while curr:  # Traverse the list until `curr` becomes None
            next_node = curr.next  # Temporarily store the next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move `prev` to the current node
            curr = next_node  # Move `curr` to the next node
        
        return prev  # At the end, `prev` will be the new head of the reversed list
        


        