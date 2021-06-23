from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        queue = deque()
        queue.append(root)

        while len(queue) != 0:

            size = len(queue)

            while size > 0:

                curr_node = queue.popleft()

                if size - 1 != 0:
                    curr_node.next = queue[0]
                else:
                    curr_node.next = None

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

                size -= 1

        return root


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.connect(root))
