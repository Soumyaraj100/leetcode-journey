class Solution(object):
    def maximumProduct(self, nums):
        m = []
        nums.sort()
        for i in xrange(len(nums) - 2):
            m.append(nums[i] * nums[i + 1] * nums[i + 2])
        m.append(nums[0] * nums[1] * nums[-1])
        return max(m)