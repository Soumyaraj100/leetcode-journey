class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=0
        for x in xrange(1,n+1):
            if x%3==0 or x%5==0 or x%7==0:
                m=m+x
        return m