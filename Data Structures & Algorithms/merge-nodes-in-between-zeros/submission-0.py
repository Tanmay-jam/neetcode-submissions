# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        prev=head
        s=0
        while temp.next:
            s+=temp.next.val
            if temp.next.val==0:
                temp.next.val=s
                s=0
                prev.next=temp.next
                prev=temp.next
            temp=temp.next
        return head.next
