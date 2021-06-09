# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd_list = ListNode(0)
        odd_list_pt = odd_list
        even_list = ListNode(0)
        even_list_pt = even_list
        count = 1

        while head:

            if count % 2 != 0:
                odd_list_pt.next = ListNode(head.val)
                odd_list_pt = odd_list_pt.next
            else:
                even_list_pt.next = ListNode(head.val)
                even_list_pt = even_list_pt.next

            head = head.next
            count += 1

        odd_list_pt.next = even_list.next

        return odd_list.next
