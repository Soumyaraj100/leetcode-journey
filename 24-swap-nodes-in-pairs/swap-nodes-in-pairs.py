class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            # swap
            prev.next = b
            a.next = b.next
            b.next = a
            # move prev forward
            prev = a
        return dummy.next

