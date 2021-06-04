# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        head = ListNode(0)
        curr = head

        remainder = 0

        while l1 and l2:
            val = l1.val + l2.val + remainder
            remainder = 0
            if val >= 10:
                val = val % 10
                remainder = 1

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + remainder
            remainder = 0
            if val >= 10:
                val = val % 10
                remainder = 1

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next

        while l2:
            val = l2.val + remainder
            remainder = 0
            if val >= 10:
                val = val % 10
                remainder = 1

            curr.next = ListNode(val)
            curr = curr.next

            l2 = l2.next

        if remainder > 0:
            curr.next = ListNode(remainder)
            curr = curr.next

        return head.next
