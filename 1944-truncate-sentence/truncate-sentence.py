class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        m=s.split()[:k]
        n=" ".join(map(str,m))
        return n