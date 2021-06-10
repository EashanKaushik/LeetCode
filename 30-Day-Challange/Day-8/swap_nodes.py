# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        curr_node = head
        next_node = head.next

        while next_node and next_node.next:
            curr_node.val, next_node.val = next_node.val, curr_node.val
            curr_node = next_node.next
            next_node = curr_node.next

        if next_node:
            curr_node.val, next_node.val = next_node.val, curr_node.val

        return head
