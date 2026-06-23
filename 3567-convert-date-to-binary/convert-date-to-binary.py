class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        s = date.split("-")
        x = "-".join(bin(int(m))[2:] for m in s)
        return x