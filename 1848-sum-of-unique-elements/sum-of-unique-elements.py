class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for x in nums:
            if nums.count(x)==1:
                s += x
        return s