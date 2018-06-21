'''
翻转一棵二叉树。

输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9


输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## 递归真是难以理解！！
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root