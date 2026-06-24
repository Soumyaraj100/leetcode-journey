class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m = 0
        k = 0
        for x in nums:
            if x == 1:
                m += 1
            else:
                if k < m:
                    k = m
                m = 0
        return max(k, m)