class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[i for i in xrange(1,n+1)]
        total = sum(nums)
        left = 0
        for i in xrange(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return nums[i]
            left += nums[i]
        return -1