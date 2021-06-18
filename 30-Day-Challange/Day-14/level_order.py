from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):

        if not root:
            return []

        q1 = deque()
        q2 = deque()
        q1.append(root)
        output = [[root.val]]

        while len(q1) != 0 or len(q2) != 0:

            if len(q1) != 0:
                q1, q2 = self.add_level(q1, q2, output)
            else:
                q2, q1 = self.add_level(q2, q1, output)

        return output

    def add_level(self, q1, q2, output):

        level_output = list()

        while len(q1) != 0:
            curr = q1.popleft()

            if curr.left:
                q2.append(curr.left)
                level_output.append(curr.left.val)

            if curr.right:
                q2.append(curr.right)
                level_output.append(curr.right.val)

        if len(level_output) != 0:
            output.append(level_output)

        return q1, q2
