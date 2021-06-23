class Solution:
    def pathSum(self, root, targetSum):

        if not root:
            return []

        stack = list()
        curr_node = root
        result = list()
        path = [root.val]

        self.dfs(root, targetSum, result, path)

        return result

    def dfs(self, root, target, result, path):

        if root:

            new_target = target - root.val

            if new_target == 0 and not root.left and not root.right:
                result.append(path.copy())

            if root.left:
                path.append(root.left.val)
                self.dfs(root.left, new_target, result, path)
                path.pop()

            if root.right:
                path.append(root.right.val)
                self.dfs(root.right, new_target, result, path)


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.pathSum(root, 3))
