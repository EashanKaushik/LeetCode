# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        curr_node = head
        curr_new = new_head = ListNode(0)
        prev = None
        while curr_node:

            if curr_node.val >= x:
                if prev:
                    prev.next = curr_node.next
                    curr_new.next = curr_node
                    curr_node = curr_node.next
                    curr_new = curr_new.next
                    curr_new.next = None

                else:
                    curr_new.next = temp = curr_node
                    head = curr_node = curr_node.next
                    temp.next = None
                    curr_new = curr_new.next

            elif curr_node.val < x:
                prev = curr_node
                curr_node = curr_node.next

        if prev:
            prev.next = new_head.next
        else:
            return new_head.next

        return head
