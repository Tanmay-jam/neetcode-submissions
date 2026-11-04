class Node:
    def __init__(self, key, value=None):
        self.key=key
        self.value=value
        self.nxt=None

class MyHashMap:

    def __init__(self):
        self.lst = [None]*1000

    def put(self, key: int, value: int) -> None:
        idx = key % 1000
        if not self.lst[idx]:
            self.lst[idx] = Node(key, value)
        else:
            temp = self.lst[idx]
            while temp:
                if temp.key == key:
                    temp.value = value
                    return
                if not temp.nxt:
                    temp.nxt = Node(key, value)
                    return
                temp = temp.nxt


    def get(self, key: int) -> int:
        idx = key%1000
        temp = self.lst[idx]
        while temp:
            if temp.key==key:
                return temp.value
            temp = temp.nxt
        return -1

    def remove(self, key: int) -> None:
        idx = key%1000
        temp = self.lst[idx]
        if not temp:
            return
        if temp.key==key:
            self.lst[idx] = temp.nxt
        else:
            while temp.nxt:
                prev = temp
                temp = temp.nxt
                if temp.key==key:
                    prev.nxt=temp.nxt
                    break
                


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)