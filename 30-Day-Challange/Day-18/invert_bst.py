# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):

        if not root:
            return

        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            size = len(queue)

            while size > 0:

                curr = queue.popleft()

                curr.left, curr.right = curr.right, curr.left

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

                size -= 1

        return root


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.invertTree(root))
