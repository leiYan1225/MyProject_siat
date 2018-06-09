'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

思路：
考察的就是二叉树的遍历，遍历每个结点然后如果重叠（两个二叉树结点都不为空）新结点值便为两者和，不重叠（只有一个结点为空）新结点值为不为空的值，全为空到达底部返跳出。
按照这个逻辑进行迭代联想：二叉树遍历方式有深度优先和广度优先，深度（纵向）优先在Python中一般使用列表，广度优先（横向）一般使用迭代
'''
# class TreeNode:
#     def __init__(self,val=None,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# tree1 = TreeNode(1,TreeNode(3,5),2)
# tree2 = TreeNode(2,TreeNode(1,right=4),TreeNode(3,right=7))
# tree3 = TreeNode()

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 结点都为空时
        if t1 is None and t2 is None:
            return
        # 只有一个结点为空时
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        # 结点重叠时
        t1.val += t2.val
        # 进行迭代
        t1.right = self.mergeTrees(t1.right, t2.right)
        t1.left = self.mergeTrees(t1.left, t2.left)
        return t1

t11 = TreeNode(1)
t12 = TreeNode(3)
t13 = TreeNode(2)
t14 = TreeNode(5)

t11.left = t12
t11.right = t13
t12.left = t14

t21 = TreeNode(2)
t22 = TreeNode(1)
t23 = TreeNode(3)
t24 = TreeNode(4)
t25 = TreeNode(7)

t21.left = t22
t21.right = t23
t22.right =t24
t24.right = t25

obj = Solution()
print(obj.mergeTrees(t11,t21))
