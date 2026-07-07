class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        e=0
        o=0
        for i in xrange(len(nums)):
            if i%2==0:
                e+=nums[i]
            else:
                o+=nums[i]
        return e-o