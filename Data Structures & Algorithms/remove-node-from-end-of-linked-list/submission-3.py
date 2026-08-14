# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        for i in range(n):
            temp=temp.next
        dummy=ListNode(next=head)
        t2=dummy
        while temp:
            temp=temp.next
            t2=t2.next
        t2.next=t2.next.next

        return dummy.next