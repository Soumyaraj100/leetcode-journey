class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = bin(n)[2:]      
        m = m.zfill(32)     
        return int(m[::-1], 2)