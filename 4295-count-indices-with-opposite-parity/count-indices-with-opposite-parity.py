class Solution(object):
    def countOppositeParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        even = 0
        odd = 0
        for i in xrange(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 0:
                ans[i] = odd
                even += 1
            else:
                ans[i] = even
                odd += 1
        return ans