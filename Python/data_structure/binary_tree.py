
# 参考博客 http://www.cnblogs.com/jiuyang/p/7928248.html
# https://www.cnblogs.com/freeman818/p/7252041.html
# 实现二叉树遍历

class Node:
    def __init__(self,value = None,left = None, right = None):
        self.value =value
        self.left = left
        self.right = right

def preTraverse(root): # 前序
    if  root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root): # 中序
    if root ==None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)

def afterTraverse(root): # 后序
    if root ==None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


def findTree(preList, midList, afterList):# 已知前、中序遍历，求后序遍历
    if len(preList) == 0:
        return
    if len(preList) == 1:
        afterList.append(preList[0])
        return
    root = preList[0]
    n = midList.index(root)
    findTree(preList[1:n + 1], midList[:n], afterList)
    findTree(preList[n + 1:], midList[n + 1:], afterList)
    afterList.append(root)
    return afterList


if __name__ == '__main__':
    if __name__ == '__main__':
        root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
        print('前序遍历：')
        preTraverse(root)
        print('中序遍历：')
        midTraverse(root)
        print('后序遍历：')
        afterTraverse(root)

        print('已知前，中序遍历求后续遍历')
        preList = list('DBACEGF')
        midList = list('ABCDEFG')
        afterList = []
        after = findTree(preList,midList,afterList)
        print(after)