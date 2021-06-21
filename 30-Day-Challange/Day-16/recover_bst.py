class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def recoverTree(self, root: TreeNode) -> None:

        first, second, prev = None, None, None

        first, second, prev = self.inorder(root, first, second, prev)

        first.val, second.val = second.val, first.val

    def inorder(self, root, first, second, prev):

            if root:

                first, second, prev = self.inorder(root.left, first, second, prev)

                if prev!=None and root.val < prev.val:
                    if not first:
                        first = prev
                    second = root

                prev = root

                first, second, prev = self.inorder(root.right, first, second, prev)

            return first, second, prev
