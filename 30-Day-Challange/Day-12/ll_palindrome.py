# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):

        if not head:
            return head

        count = 1
        temp = head
        while temp.next:
            count += 1
            temp = temp.next

        curr_count = 0
        stack = list()
        temp = head

        while curr_count != count // 2:
            stack.append(temp.val)
            temp = temp.next
            curr_count += 1

        if count % 2 != 0:
            temp = temp.next

        while temp:

            if temp.val != stack.pop():
                return False

            temp = temp.next

        return True
