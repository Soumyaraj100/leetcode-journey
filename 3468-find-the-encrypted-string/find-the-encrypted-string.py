class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        k=k%len(s)
        y=s+s
        x=""
        for i in xrange(len(s)):
            x+=y[i+k]
        return x