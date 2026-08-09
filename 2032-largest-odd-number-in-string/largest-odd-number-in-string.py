class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        while num:
            if int(num[-1]) % 2 == 0:
                num = num[:len(num)-1]
            else:
                return num
        return ""
        
