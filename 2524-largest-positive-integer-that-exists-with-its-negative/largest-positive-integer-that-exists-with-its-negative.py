class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -1
        for x in nums:
            if -x in nums and x > max:
                max = x
        return max