class Solution:
        
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        Nmap={}
        children = set()
        for pair in descriptions:
            if pair[0] not in Nmap:
                Nmap[pair[0]] = TreeNode(pair[0])
            if pair[1] not in Nmap:
                Nmap[pair[1]] = TreeNode(pair[1])
            if pair[2]:
                Nmap[pair[0]].left = Nmap[pair[1]]
            else:
                Nmap[pair[0]].right = Nmap[pair[1]]
            children.add(pair[1])
        
        for val, node in Nmap.items():
            if val not in children:
                root = node
        return root
        