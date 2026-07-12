class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=b=0
        for x in nums:
            if x<10:
                a+=x
            else:
                b+=x
        if a==b:
            return False
        return True