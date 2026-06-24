class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = bin(num)[2:]
        r = ""
        for i in s:
            if i == "0":
                r += "1"
            else:
                r += "0"
        return int(r, 2)