class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        c=0
        for x in nums:
            c+=str(x).count(str(digit))
        return c