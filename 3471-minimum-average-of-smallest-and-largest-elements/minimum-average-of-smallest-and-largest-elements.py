class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        s = []
        while nums:
            a = nums.pop(nums.index(min(nums)))
            b = nums.pop(nums.index(max(nums)))
            s.append((a + b) / 2.0)
        return min(s)