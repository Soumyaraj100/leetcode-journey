class Solution(object):
    def findTheArrayConcVal(self, nums):
        ans = 0
        while len(nums) > 1:
            ans += int(str(nums.pop(0)) + str(nums.pop()))
        if nums:
            ans += nums[0]
        return ans