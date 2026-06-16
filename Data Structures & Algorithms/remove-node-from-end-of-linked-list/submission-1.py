# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        temp=head
        while temp:
            sz+=1
            temp = temp.next
        nodefromstart = sz - n +1

        if sz==1 and nodefromstart==1:
            return None

        curr, prev = head, None
        for i in range(nodefromstart-1):
            prev = curr
            curr = curr.next
        if not curr.next:
            prev.next = None
        else:
            curr.val = curr.next.val
            curr.next = curr.next.next
        return head
            