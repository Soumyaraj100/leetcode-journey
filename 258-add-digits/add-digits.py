class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            s = 0
            for digit in str(num):
                s += int(digit)
            num = s
        return num