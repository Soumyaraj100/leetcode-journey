# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if count == n:
            return head.next
        curr = head
        for _ in range(count - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head