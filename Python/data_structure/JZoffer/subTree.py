## 树的子结构

class Node:
    def __init__(self,value = None,left = None, right = None):
        self.value =value
        self.left = left
        self.right = right

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.isSubtree(pRoot1, pRoot2)

    def isSubtree(self, p1, p2):
        if p2 == None:
            return True
        if p1 == None:
            return p1 == p2
        res = False
        if p1.val == p2.val:
            res = self.isSubtree(p1.left, p2.left) and self.isSubtree(p1.right, p2.right)
        return res or self.isSubtree(p1.left, p2) or self.isSubtree(p1.right, p2)