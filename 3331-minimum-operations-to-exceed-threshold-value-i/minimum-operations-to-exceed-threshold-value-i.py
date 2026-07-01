class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = []
        nums.sort()
        for x in nums:
            if x < k:
                c.append(x)
        return len(c)