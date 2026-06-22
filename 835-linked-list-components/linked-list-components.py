class Solution(object):
    def numComponents(self, head, nums):
        s = set(nums)
        ans = 0
        while head:
            if head.val in s and (head.next is None or head.next.val not in s):
                ans += 1
            head = head.next
        return ans