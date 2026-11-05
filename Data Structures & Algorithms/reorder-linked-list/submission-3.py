# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst=[]
        temp=head
        while temp:
            lst.append(temp)
            temp=temp.next
            lst[-1].next=None
        dummy=ListNode()
        temp=dummy
        i=0
        j=len(lst)-1
        while i<j:
            temp.next = lst[i]
            temp=temp.next
            temp.next = lst[j]
            temp=temp.next
            i+=1
            j-=1
        if i==j:
            temp.next=lst[i]
