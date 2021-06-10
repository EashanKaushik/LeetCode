# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        curr_node = next_node = head
        index = 0
        head_found = False
        first_carry = None

        while next_node and curr_node.next:

            while index < k and next_node:
                if not head_found:
                    head = next_node
                prev = next_node = next_node.next
                index += 1

            head_found = True

            if index < k:
                break

            first = curr_node

            while curr_node != next_node:
                temp = curr_node.next
                curr_node.next = prev
                prev = curr_node
                curr_node = temp

            if not first_carry:
                first_carry = first
                index = 0
                continue

            first_carry.next = prev
            first_carry = first

            curr_node = next_node
            index = 0

        return head
