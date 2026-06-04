class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=[]
        for i in xrange(len(nums)):
            if nums[i]%2==0:
                m.append(nums[i])
        for i in xrange(len(nums)):
            if nums[i]%2!=0:
                m.append(nums[i])
        return m