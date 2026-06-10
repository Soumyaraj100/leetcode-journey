class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m=[]
        for x in nums:
            if nums.count(x)==1:
                m.append(x)
        return m