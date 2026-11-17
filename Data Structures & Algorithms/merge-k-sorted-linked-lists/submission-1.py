# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, l1, l2):
        temp = dummyNode = ListNode()
        while l1 and l2:
            if l1.val<=l2.val:
                temp.next = l1
                l1=l1.next
            else:
                temp.next = l2
                l2=l2.next
            temp=temp.next
        temp.next = l1 if l1 else l2
        return dummyNode.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            mergedList=[]
            for i in range(0,len(lists),2):
                if i==len(lists)-1:
                    newList=lists[i]
                else:
                    newList = self.merge(lists[i], lists[i+1])
                mergedList.append(newList)
            lists = mergedList
        return lists[0]