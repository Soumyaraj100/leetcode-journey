class Solution(object):
    def dominantIndex(self, nums):
        num = nums[:]
        num.sort()
        for x in num[:-1]:
            if x * 2 > num[-1]:
                return -1
        return nums.index(num[-1])