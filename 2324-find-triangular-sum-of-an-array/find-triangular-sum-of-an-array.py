class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums)!=1:
            temp=[]
            for i in xrange(len(nums)-1):
                temp.append((nums[i]+nums[i+1])%10)
            nums=temp
        return nums[0]
        