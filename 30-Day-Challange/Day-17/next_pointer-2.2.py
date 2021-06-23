# Definition for a Node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Node') -> 'Node':

        head = root

        while head:

            dummy_head = dummy = Node(0)
            while head:

                if head.left:
                    dummy.next = head.left
                    dummy = dummy.next

                if head.right:
                    dummy.next = head.right
                    dummy = dummy.next

                head = head.next

            head = dummy_head.next

        return root


s = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.right = TreeNode(4)
root.right.right = TreeNode(4)

print(s.connect(root))
