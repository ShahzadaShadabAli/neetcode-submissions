# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        this = head
        while this:
            leng+=1
            this = this.next
        if leng <= n:
            n = n%leng
        else:
            n = leng - n
        if n == 0:
            return head.next
        count = 0
        prev = None
        current = head
        while current and count < n:
            print(current.val)
            prev = current
            current = current.next
            count+=1
        prev.next = current.next
        return head

        # dummy = ListNode(0, head)
        # left = dummy
        # right = head

        # while n>0 and right:
        #     right = right.next
        #     n-=1

        # while right:
        #     left = left.next
        #     right = right.next

        # left.next = left.next.next
        # return dummy.next