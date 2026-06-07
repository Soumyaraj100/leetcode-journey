class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in xrange(len(nums)):
            if len(str(nums[i]))%2==0:
                s=s+1
        return s