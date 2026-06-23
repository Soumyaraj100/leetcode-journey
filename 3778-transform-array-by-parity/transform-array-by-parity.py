class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for x in nums:
            if x%2==0:
                a.append(0)
            else:
                a.append(1)
        a.sort()
        return a