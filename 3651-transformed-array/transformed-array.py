class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        ans = [0] * n
        for i in xrange(n):
            ans[i] = nums[(i + nums[i]) % n]
        return ans