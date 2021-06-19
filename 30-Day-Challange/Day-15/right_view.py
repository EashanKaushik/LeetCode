from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):

        if not root:
            return root

        queue = deque()
        queue.append(root)
        output = list()
        count = len(queue)

        while len(queue) != 0:

            curr_node = queue.popleft()
            count -= 1

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            if count == 0:
                output.append(curr_node.val)
                count = len(queue)

        return output

s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.rightSideView(root))
