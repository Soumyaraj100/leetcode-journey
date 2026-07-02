class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)/2
        for x in nums:
            if nums.count(x)==n:
                return x