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
        if not head:
            return head
        mapp={}
        temp=head
        while temp:
            newnode = Node(x=temp.val)
            mapp[temp]=newnode
            temp=temp.next
        node=head
        while node:
            if node.next:
                mapp[node].next=mapp[node.next]
            else:
                mapp[node].next=None
            if node.random:
                mapp[node].random=mapp[node.random]
            else:
                mapp[node].random=None
            node=node.next
        return mapp[head]