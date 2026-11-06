# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA, tempB = headA, headB
        rot=3
        while rot:
            rot = rot-1 if (tempA.next==None or tempB.next==None) else rot
            if tempA==tempB:
                return tempA
            tempA = tempA.next if tempA.next else headB
            tempB = tempB.next if tempB.next else headA