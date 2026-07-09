class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=list(s)
        s[:k]=s[:k][::-1]
        s="".join(map(str,s))
        return s
        