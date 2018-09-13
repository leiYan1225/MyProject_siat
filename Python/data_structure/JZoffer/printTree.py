## 从上到下打印二叉树


class Node():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def solution(root):
    queue= []
    result = []
    if root == None:
        return result
    queue.append(root) ## 注意进queue的是节点，而不是val
    while queue:
        newNode = queue.pop(0)
        result.append(newNode.val)  # 存进result的才是val
        if newNode.left != None:
            queue.append(newNode.left)
        if newNode.right != None:
            queue.append(newNode.right)
