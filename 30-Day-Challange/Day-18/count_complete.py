# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root):

        if not root:
            return 0

        count = 0
        queue = deque()

        queue.append(root)

        while len(queue) != 0:

            size = len(queue)

            while size > 0:
                count += 1
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                else:
                    break
                if curr.right:
                    queue.append(curr.right)
                else:
                    break
                size -= 1

        return count


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.countNodes(root))
