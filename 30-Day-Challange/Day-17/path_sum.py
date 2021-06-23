class Solution:
    def hasPathSum(self, root, targetSum):

        output = list()
        output.append(False)

        self.dfs(root, targetSum, output)

        return output[-1]

    def dfs(self, root, target, output):

        if root and not output[-1]:

            new_target = target - root.val

            if new_target == 0 and not root.left and not root.right:
                output.append(True)

            self.dfs(root.left, new_target, output)

            if output[-1]:
                return

            self.dfs(root.right, new_target, output)


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.hasPathSum(root, 7))
