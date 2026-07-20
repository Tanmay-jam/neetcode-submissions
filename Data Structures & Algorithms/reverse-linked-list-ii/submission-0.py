# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = ListNode(next=head)
        dummy = prev
        for i in range(1, left):
            prev=prev.next
        temp = prev
        curr = prev.next

        for j in range(right-left+1):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        temp.next.next = curr
        temp.next = prev
        return dummy.next