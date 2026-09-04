class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in xrange(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1  
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target - s) < abs(target - closest):
                    closest = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s
        return closest