class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i=0
        nums.sort()
        while i<=len(nums):
            nums[i:i+2]=nums[i:i+2][::-1]
            i+=2
        return nums