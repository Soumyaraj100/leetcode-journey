class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        m=[]
        for i in xrange(n+1):
            s=str(bin(i)).count("1")
            m.append(s)
        return m