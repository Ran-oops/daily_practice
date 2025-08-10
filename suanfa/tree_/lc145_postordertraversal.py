from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        results = []

        def dfs(node):
            nonlocal results
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            results.append(node.val)

        dfs(root)
        return results

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node3
node1.right = node2

s = Solution().postorderTraversal(node1)
print(s)