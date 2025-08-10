class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # write code here
        if not t1:
            return t2
        if not t2:
            return t1

        # 根左右的方式递归
        head = TreeNode(t1.val + t2.val)
        head.left = self.mergeTrees(t1.left, t2.left)
        head.right = self.mergeTrees(t1.right, t2.right)

        return head