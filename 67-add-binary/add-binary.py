class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r1 = int(a, 2)
        r2 = int(b, 2)
        return str(bin(r1+r2)).replace("0b","")