# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        
        # Traverse the linked list and collect values
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Check if the list of values is a palindrome
        return values == values[::-1]
        