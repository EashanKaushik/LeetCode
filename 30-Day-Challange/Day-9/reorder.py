# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        size= 0
        vals = []
        tmp = head
        flag = True
        while(tmp):
            size += 1
            vals.append(tmp.val)
            tmp = tmp.next

        start = 0
        tmp = head
        end = size
        while(tmp):
            if(flag):
                tmp.val = vals[start]
                end = end - 1
                flag = False
            else:
                tmp.val = vals[end]
                start = start + 1
                flag = True
            tmp = tmp.next
