class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):

        head = None

        while l1 and l2:
            if l1.val <= l2.val:
                if not head:
                    head = ListNode(l1.val)
                else:
                    curr_node = head
                    while curr_node.next != None:
                        curr_node = curr_node.next

                    curr_node.next = ListNode(l1.val)

                l1 = l1.next

            elif l1.val > l2.val:
                if not head:
                    head.val = ListNode(l2.val)
                else:
                    curr_node = head
                    while curr_node.next != None:
                        curr_node = curr_node.next

                    curr_node.next = ListNode(l2.val)

                l2 = l2.next

        while l1:
            curr_node = head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = ListNode(l1.val)

            l1 = l1.next

        while l2:
            curr_node = head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = ListNode(l2.val)

            l2 = l2.next

        while head:
            print(head.val)
            head = head.next

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
s.mergeTwoLists(l1, l2)
