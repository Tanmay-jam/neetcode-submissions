# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = ListNode()
        f = s
        f.next = head
        while f and f.next:
            s = s.next
            f = f.next.next
        t1 = head
        t2 = s.next
        s.next = None

        #reverse second ll
        if not t2:
            pass
        else:
            prev, curr, nex = None, t2, t2.next
            while curr.next:
                curr.next = prev
                prev = curr
                curr = nex
                nex = nex.next
            curr.next = prev
            t2 = curr

            #merge two lls
            newhead = ListNode()
            temp = newhead
            while t1 and t2:
                temp.next = t1
                temp = temp.next
                t1 = t1.next
                temp.next = t2
                temp = temp.next
                t2 = t2.next
            if t1:
                temp.next = t1
            
            head = newhead.next



        