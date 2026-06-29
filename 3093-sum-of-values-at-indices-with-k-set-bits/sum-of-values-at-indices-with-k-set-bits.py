class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        s = 0
        for i in range(len(nums)):
            if bin(i).count("1") == k:
                s += nums[i]
        return s