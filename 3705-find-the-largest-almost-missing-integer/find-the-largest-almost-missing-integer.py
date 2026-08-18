class Solution(object):
    def largestInteger(self, nums, k):
        if k == 1:
            unique = [x for x in nums if nums.count(x) == 1]
            return max(unique) if unique else -1
        if k == len(nums):
            return max(nums)
        a = nums[0]
        b = nums[-1]
        if nums.count(a) == 1 and nums.count(b) == 1:
            return max(a, b)
        elif nums.count(a) == 1:
            return a
        elif nums.count(b) == 1:
            return b
        else:
            return -1