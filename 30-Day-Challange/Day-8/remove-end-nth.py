# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):

        len_ll = 0
        curr_node = head

        while (curr_node):
            len_ll += 1
            curr_node = curr_node.next


        len_ll = len_ll - n
        curr_node = head

        if len_ll == 0:
            if head.next:
                head = head.next
            else:
                head = None

            return head

        while len_ll > 1 and curr_node:
            len_ll -= 1
            curr_node = curr_node.next

        curr_node.next = curr_node.next.next

        return head
