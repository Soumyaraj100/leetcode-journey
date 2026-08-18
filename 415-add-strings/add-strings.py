class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))
        num1 = list(num1)
        num2 = list(num2)
        res = ""
        n = 0
        while num1:
            r = (int(num1[-1]) + int(num2[-1]) + n) % 10
            n = (int(num1[-1]) + int(num2[-1]) + n) // 10
            num1.pop()
            num2.pop()
            res += str(r)
        if n:
            res += str(n)
        return res[::-1]