class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n:
            if set(bin(n)[2:])=={"1"}:
                return n
            n+=1