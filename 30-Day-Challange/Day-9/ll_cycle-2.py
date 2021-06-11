# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head:
            return head

        fast = head
        unique = set()

        while 1:

            if fast.next == None:
                return

            if fast not in unique:
                unique.add(fast)
            else:
                return fast

            fast = fast.next
