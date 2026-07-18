class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        min_sum = sum(nums[:k])
        max_sum = sum(nums[-k:])
        return abs(max_sum - min_sum)