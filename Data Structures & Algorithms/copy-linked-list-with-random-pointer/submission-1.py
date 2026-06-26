"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = { None:None }

        curr = head
        while curr:
            copyNode = Node(curr.val)
            res[curr] = copyNode
            curr = curr.next

        curr = head
        while curr:
            copyNode = res[curr]
            copyNode.next = res[curr.next]
            copyNode.random = res[curr.random]
            curr = curr.next

        return res[head]