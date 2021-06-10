# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'Value: {self.val} & Next --> ({self.next})'


class Solution:
    def rotateRight(self, head, k):

        if not head or not head.next:
            return head

        count = 0
        first = True
        while k > 0:
            curr_node = head
            next_node = head
            prev = None

            while next_node.next:
                prev = next_node
                next_node = next_node.next
                count += 1

            if first:
                first = False
                k = k % (count + 1)

                if k == 0:
                    break

            prev.next = None
            next_node.next = curr_node
            head = next_node

            k -= 1

        return head


if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(head)

    s = Solution()
    print(s.rotateRight(head, 2))
