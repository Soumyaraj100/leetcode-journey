class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        for i in xrange(len(nums)):
            s.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return s