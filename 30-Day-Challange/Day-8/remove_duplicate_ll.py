# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def deleteDuplicates(self, head):

        if not head:
            return head

        curr_node = head

        while curr_node.next:

            duplicate = curr_node.next

            while curr_node.val == duplicate.val:
                if duplicate.next == None:
                    duplicate = None
                    break
                else:
                    duplicate = duplicate.next

            curr_node.next = duplicate

            curr_node = curr_node.next
            if not curr_node:
                break

        return head
