# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        s = []
        for i in xrange(len(lists)):
            curr = lists[i]
            while curr:
                s.append(curr.val)
                curr = curr.next
        s.sort()
        if not s:
            return None
        dum = ListNode(0)
        curr = dum
        for x in s:
            curr.next = ListNode(x)
            curr = curr.next
        return dum.next
