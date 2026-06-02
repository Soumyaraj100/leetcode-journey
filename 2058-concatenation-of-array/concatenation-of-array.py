class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if 1 <= len(nums) <= 1000:
            for i in xrange(len(nums)):
                if 1 <= nums[i] <= 1000:
                    nums.append(nums[i])
        return nums