# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        m=[]
        curr=head
        n=0
        while curr:
            m.append(curr.val)
            curr=curr.next
        for i in xrange(len(m)):
            n += m[i] * (2 ** (len(m) - 1 - i))
        return n