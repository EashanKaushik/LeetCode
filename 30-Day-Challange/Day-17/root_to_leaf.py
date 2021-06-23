# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        result = list()
        path = [str(root.val)]

        self.dfs(root, result, path)

        return sum(result)

    def dfs(self, root, result, path):

        if root:

            if not root.left and not root.right:
                # leaf
                curr_path = path.copy()
                result.append(int(''.join(curr_path)))

            if root.left:
                path.append(str(root.left.val))
                self.dfs(root.left, result, path)
                path.pop()

            if root.right:
                path.append(str(root.right.val))
                self.dfs(root.right, result, path)
                path.pop()


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.sumNumbers(root))
