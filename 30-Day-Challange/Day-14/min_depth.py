import sys
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        min_depth = sys.maxsize
        queue = deque()
        queue.append((root, 1))

        while len(queue) > 0:

            curr_node, depth = queue.popleft()

            if not curr_node.left and not curr_node.right:
                return depth

            else:
                if curr_node.left:
                    queue.append((curr_node.left, depth + 1))

                if curr_node.right:
                    queue.append((curr_node.right, depth + 1))


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.minDepth(root))
