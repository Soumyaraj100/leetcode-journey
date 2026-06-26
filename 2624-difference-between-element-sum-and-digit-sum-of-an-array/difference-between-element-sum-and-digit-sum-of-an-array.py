class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=[]
        for x in nums:
            if x == 0:
                s.append(0)
            while x!=0:
                s.append(x%10)
                x=x//10
        return abs(sum(nums)-sum(s))