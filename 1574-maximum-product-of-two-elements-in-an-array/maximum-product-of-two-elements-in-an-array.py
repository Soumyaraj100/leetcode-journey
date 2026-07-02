class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x=nums.pop()
        y=nums.pop()
        return (x-1)*(y-1)
