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
        temp=head
        dummy = newNode = Node(101)
        nmap={}
        while temp:
            newNode.next = Node(temp.val)
            newNode=newNode.next
            nmap[temp]=newNode
            temp=temp.next
        temp=head
        newNode=dummy.next
        while temp:
            newNode.random = nmap[temp.random] if temp.random else None
            newNode, temp = newNode.next, temp.next
        return dummy.next
