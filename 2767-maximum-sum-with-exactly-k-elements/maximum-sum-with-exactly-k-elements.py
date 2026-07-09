class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        score = 0
        for i in range(k):
            score += mx
            mx += 1
        return score