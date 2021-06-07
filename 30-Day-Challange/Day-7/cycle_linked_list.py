class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):

        if not head or not head.next:
            return False

        curr_node = head
        values_seen = set()

        while curr_node:
            val = hash(curr_node)
            if val in values_seen:
                return True
            else:
                values_seen.add(val)

            curr_node = curr_node.next


        return False
