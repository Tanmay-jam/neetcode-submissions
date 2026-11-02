class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.lst = [None]*1000

    def add(self, key: int) -> None:
        idx = key%1000
        if not self.lst[idx]:
            self.lst[idx]=Node(key)
        else:
            temp = self.lst[idx]
            while temp.next:
                if temp.val==key:
                    return
                temp = temp.next
            temp.next = Node(key) if temp.val!=key else None

    def remove(self, key: int) -> None:
        idx = key%1000
        if not self.lst[idx]:
            return
        if self.lst[idx].val==key:
            self.lst[idx] = self.lst[idx].next
        else:
            temp = self.lst[idx].next
            prev = self.lst[idx]
            while temp!=None:
                if temp.val==key:
                    prev.next = temp.next
                    break
                prev = temp
                temp = temp.next

    def contains(self, key: int) -> bool:
        idx = key%1000
        temp = self.lst[idx]
        while temp:
            if temp.val==key:
                return True
            temp = temp.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)