class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res=[]
        x="0b"
        for i in xrange(len(nums)):
            x+=str(nums[i])
            res.append(int(x,2)%5==0)
        return res