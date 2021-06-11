# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return head

        # find mid
        slow = head
        fast = head
        prev = None

        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)

        if prev:
            prev.next = None
            root.left = self.sortedListToBST(head)
        else:
            root.left = self.sortedListToBST(None)

        temp = slow.next
        slow.next = None


        root.right = self.sortedListToBST(temp)

        return root
