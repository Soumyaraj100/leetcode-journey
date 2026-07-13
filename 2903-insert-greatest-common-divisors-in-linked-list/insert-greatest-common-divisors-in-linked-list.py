class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        curr = head
        while curr and curr.next:
            g = math.gcd(curr.val, curr.next.val)
            newNode = ListNode(g)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next
        return head