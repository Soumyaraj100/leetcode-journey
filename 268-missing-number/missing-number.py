class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        e = n * (n + 1) // 2
        a = sum(nums)
        return e - a