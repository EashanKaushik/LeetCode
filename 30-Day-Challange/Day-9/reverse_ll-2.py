# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        curr_node = head
        count = 1
        prev = None

        while curr_node:

            if count == left:

                next_node = curr_node

                while count != right:
                    next_node = next_node.next
                    count += 1


                if prev:
                    while curr_node != next_node:
                        temp = prev.next = curr_node.next
                        curr_node.next = next_node.next
                        next_node.next = curr_node
                        curr_node = temp
                else:
                    while curr_node != next_node:
                        temp = curr_node.next
                        curr_node.next = next_node.next
                        next_node.next = curr_node
                        head = curr_node = temp

                break

            prev = curr_node
            curr_node = curr_node.next
            count += 1

        return head
