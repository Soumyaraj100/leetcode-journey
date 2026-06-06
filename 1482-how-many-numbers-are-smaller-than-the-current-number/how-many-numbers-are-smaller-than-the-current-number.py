class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=sorted(nums)
        s=[]
        for i in xrange(len(nums)):
            s.append(m.index(nums[i]))
        return s