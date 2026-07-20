class Solution(object):
    def mergeNodes(self, head):
        ans = []
        curr = head.next
        s = 0

        while curr:
            if curr.val == 0:
                ans.append(s)
                s = 0
            else:
                s += curr.val

            curr = curr.next

        dummy = ListNode(0)
        cur = dummy

        for x in ans:
            cur.next = ListNode(x)
            cur = cur.next

        return dummy.next