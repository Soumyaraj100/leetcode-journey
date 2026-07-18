class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        b=0
        for x in nums:
            c+=x
            if c==0:
                b+=1
        return b