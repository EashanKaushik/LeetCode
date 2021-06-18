class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        queue = deque()
        queue.append(root)
        queue.append(root)

        while len(queue) != 0:

            t1 = queue.popleft()
            t2 = queue.popleft()

            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False

            queue.append(t1.left)
            queue.append(t2.right)

            queue.append(t1.right)
            queue.append(t2.left)

        return True


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.isSymmetric(root))
