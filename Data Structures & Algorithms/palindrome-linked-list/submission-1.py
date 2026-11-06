# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        prev=s
        while f and f.next:
            prev = s
            s, f = s.next, f.next.next
        prev.next=None
        prev, curr = None, s
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        start, end = head, prev
        while start:
            if start.val!=end.val:
                return False
            start, end = start.next, end.next
        return True
        