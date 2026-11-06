# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total=temp=ListNode()
        carry=0
        while l1 or l2:
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            digit = (n1 + n2 + carry)%10
            carry = (n1 + n2 + carry)//10
            temp.next = ListNode(digit)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            temp = temp.next
        temp.next = ListNode(carry) if carry else None
        return total.next
