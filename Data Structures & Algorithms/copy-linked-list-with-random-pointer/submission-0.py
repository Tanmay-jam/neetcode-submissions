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
        temp = head
        oldtonew={None:None}
        while temp:
            oldtonew[temp] = Node(x=temp.val)
            temp = temp.next
        temp=head
        while temp:
            oldtonew[temp].next = oldtonew[temp.next]
            oldtonew[temp].random = oldtonew[temp.random]
            temp = temp.next
        return oldtonew[head]
