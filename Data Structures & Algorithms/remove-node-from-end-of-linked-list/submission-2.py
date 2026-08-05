# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        temp=head
        for i in range(n):
            temp = temp.next
        temp2=dummy
        while temp:
            temp=temp.next
            temp2=temp2.next
        temp2.next=temp2.next.next
        return dummy.next

