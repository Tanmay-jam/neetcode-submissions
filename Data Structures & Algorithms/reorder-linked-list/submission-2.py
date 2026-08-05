# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        lst = []
        while temp:
            lst.append(temp)
            temp=temp.next
        
        s, e = 0, len(lst)-1
        while s<e:
            lst[s].next = lst[e]
            s+=1
            if s==e:
                break
            lst[e].next = lst[s]
            e-=1
        lst[s].next=None