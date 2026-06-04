import bisect
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        m=bisect.bisect_left(nums,target)
        if m < len(nums) and nums[m]==target:
            return m
        return -1