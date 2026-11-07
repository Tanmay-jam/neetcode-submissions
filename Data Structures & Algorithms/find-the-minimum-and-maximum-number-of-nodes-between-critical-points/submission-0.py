# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        temp, prev = head.next, head
        index=1
        while temp.next:
            if (prev.val<temp.val and temp.val>temp.next.val) or (prev.val>temp.val and temp.val<temp.next.val):
                arr.append(index)
            temp=temp.next
            prev=prev.next
            index+=1
        if len(arr)<2:
            return [-1, -1]
        mindiff, maxdiff = arr[-1]-arr[0], arr[-1]-arr[0]
        for i in range(len(arr)-1):
            mindiff = min(mindiff, arr[i+1]-arr[i])
        return [mindiff, maxdiff]