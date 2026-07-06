class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        for i in xrange(len(nums)):
            c = 0
            x = nums[i]
            while x:
                c += x % 10
                x //= 10
            s.append(c)
        for i in xrange(len(s)):
            if i == s[i]:
                return i
        return -1