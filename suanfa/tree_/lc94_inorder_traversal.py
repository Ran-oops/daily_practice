class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        results = []
        def dfs(node):
            nonlocal  results
            if not node:
                return 
            dfs(node.left)
            results.append(node.val)
            dfs(node.right)
        dfs(root)
        return results



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.right = node3
node1.left = node2

s = Solution().inorderTraversal(node1)
print(s)
