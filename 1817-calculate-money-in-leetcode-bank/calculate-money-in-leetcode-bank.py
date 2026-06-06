class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        for i in xrange(n):
                s=s+i//7+i%7+1
        return s
