class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')
        zeros = s.count('0')
        return '1' * (ones - 1) + '0' * zeros + '1'