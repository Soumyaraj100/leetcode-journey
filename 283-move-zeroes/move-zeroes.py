class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=nums.count(0)
        for i in xrange(n):
            nums.remove(0)
        for i in xrange(n):
            nums.append(0*i)