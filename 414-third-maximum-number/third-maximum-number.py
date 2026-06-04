class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        for k in xrange(2): 
            nums.remove(max(nums))
        return max(nums)