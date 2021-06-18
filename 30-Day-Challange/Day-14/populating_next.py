from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        output = list()
        queue = deque()

        queue.append((root, 0))

        while len(queue) > 0:

            curr_node, level = queue.popleft()

            if len(queue) == 0:
                curr_node.next = None
            elif queue[0][1] != level:
                curr_node.next = None
            else:
                curr_node.next = queue[0][0]

            if curr_node.left:
                queue.append((curr_node.left, level + 1))

            if curr_node.right:
                queue.append((curr_node.right, level + 1))

        return root


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.connect(root))
