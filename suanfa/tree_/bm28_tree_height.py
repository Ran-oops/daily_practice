class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self , root: TreeNode) -> int:
        if not root:
            return 0
        return  max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.right = node3
node1.left = node2

s = Solution().maxDepth(node1)
print(s)
