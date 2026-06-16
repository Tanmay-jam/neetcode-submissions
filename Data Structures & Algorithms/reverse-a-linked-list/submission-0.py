# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp, prev, new = head, None, head.next
        while new:
            temp.next = prev
            prev = temp
            temp = new
            new = new.next
        temp.next = prev
        return temp