class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        stack1 = list()
        stack2 = list()
        output = list()
        stack1.append(root)

        while len(stack1) > 0 or len(stack2) > 0:

            curr_output = list()

            if len(stack1) > 0:
                while len(stack1) > 0:

                    curr_node = stack1.pop()
                    curr_output.append(curr_node.val)

                    if curr_node.left:
                        stack2.append(curr_node.left)

                    if curr_node.right:
                        stack2.append(curr_node.right)

            else:
                while len(stack2) > 0:

                    curr_node = stack2.pop()
                    curr_output.append(curr_node.val)

                    if curr_node.right:
                        stack1.append(curr_node.right)

                    if curr_node.left:
                        stack1.append(curr_node.left)

            output.append(curr_output)

        return output


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.zigzagLevelOrder(root))
