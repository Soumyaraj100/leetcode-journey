class Solution(object):
    def sortColors(self, nums):
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]