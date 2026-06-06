class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        for i in xrange(1,n+1):
            if n%i==0:
                s=s+1
        return s==3