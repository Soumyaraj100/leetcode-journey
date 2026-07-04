class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        for i in xrange(len(s)):
            m+=(123-ord(s[i]))*(i+1)
        return m