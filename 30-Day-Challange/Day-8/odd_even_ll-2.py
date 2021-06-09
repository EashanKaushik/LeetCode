# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):

        if not head or not head.next or not head.next.next:
            return head

        odd_pt = odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next = even.next
            odd_pt = odd
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd_pt.next.next = even_head

        return head
