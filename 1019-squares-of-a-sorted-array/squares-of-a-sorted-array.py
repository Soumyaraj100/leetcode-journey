class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n
        l = 0
        r = n - 1
        i = n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l] * nums[l]
                l += 1
            else:
                ans[i] = nums[r] * nums[r]
                r -= 1
            i -= 1
        return ans