class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        m=[]
        for x in nums:
            s+=list(str(x))
        for ch in s:
            m.append(int(ch))
        return m