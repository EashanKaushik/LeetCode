# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        stack = list()
        curr_node = root
        op = list()

        while len(stack) > 0 or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                op.append(curr_node.val)
                curr_node = curr_node.right

        if op == sorted(op) and len(op) == len(set(op)):
            return True

        return False


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.isValidBST(root))
