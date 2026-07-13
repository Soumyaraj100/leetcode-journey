class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for x in set(nums):
            if nums.count(x)==2:
                s^=x
        return s