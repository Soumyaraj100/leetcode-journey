class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=0
        for i in xrange(len(nums)-1):
            for j in xrange(i+1,len(nums)):
                if (nums[i]-1)*(nums[j]-1)>m:
                    m=(nums[i]-1)*(nums[j]-1)
        return m
