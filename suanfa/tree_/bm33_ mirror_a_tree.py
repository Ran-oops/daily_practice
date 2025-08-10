class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        if not pRoot:
            return pRoot

        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)

        return pRoot

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(6)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(5)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
s = Solution()
r = s.Mirror(a)
print(r)
print(r.left.val)