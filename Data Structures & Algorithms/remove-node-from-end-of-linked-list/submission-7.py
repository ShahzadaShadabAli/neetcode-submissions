# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        dummy = ListNode()
        pointer = dummy
        for i in range(n):
            right = right.next
        while right:
            pointer.next = left
            right = right.next
            left = left.next
            pointer = pointer.next
        pointer.next = left.next
        pointer = pointer.next
        return dummy.next
        
        