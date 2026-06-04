class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=nums[0]
        for i in xrange(1,len(nums)):
            m=m^nums[i]
        return m