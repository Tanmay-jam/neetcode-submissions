# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        start = dummy
        for i in range(a):
            start=start.next
        temp=start.next
        start.next = list2
        for i in range(b-a):
            temp=temp.next
        while list2.next:
            list2=list2.next
        list2.next=temp.next
        return dummy.next