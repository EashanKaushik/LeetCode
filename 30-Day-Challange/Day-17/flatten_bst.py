# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:

        self.postorder(root)

        return root

    def postorder(self, root):

        if root:

            self.postorder(root.right)

            self.postorder(root.left)

            root.right = self.prev

            root.left = None

            self.prev = root


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.flatten(root))