class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ds=0
        ss=0
        while n:
            ds+=n%10
            ss+=(n%10)**2
            n=n//10
        return ss-ds>=50