# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        curr_node = head
        prev = None

        while curr_node.next:

            if curr_node.val == curr_node.next.val:
                duplicate = curr_node.next
                while curr_node.val == duplicate.val:
                    if duplicate.next == None:
                        if prev:
                            prev.next = None
                            curr_node = prev
                        else:
                            return None

                        return head
                    else:
                        duplicate = duplicate.next

                if prev == None:
                    curr_node = head = duplicate
                else:
                    curr_node = prev.next = duplicate


            else:
                prev = curr_node
                curr_node = curr_node.next

        return head
        
