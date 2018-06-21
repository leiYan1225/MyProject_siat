
'''
参考博客  https://www.cnblogs.com/freeman818/p/7252041.html
实现二叉树遍历

例子：
	     D
	    / \
	   B   E
	  / \   \
	 A   C   G
	        /
	       F
'''


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
    root = preList[0]  #先序的第一个节点即根节点
    n = midList.index(root) #找到根节点在中序中对应的index
    findTree(preList[1:n + 1], midList[:n], afterList) #对左子树采取相同的操作
    findTree(preList[n + 1:], midList[n + 1:], afterList) #对右子树采取相同操作
    afterList.append(root)  #只有到叶子节点时才加到afterList中，顺序也是先左后右，最后才是往上递归到根节点
    return afterList


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