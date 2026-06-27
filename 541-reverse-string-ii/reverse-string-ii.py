class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n=0
        l=list(s)
        while n<len(l):
            l[n:n+k]=l[n:n+k][::-1]
            n+=2*k
        return "".join(map(str,l))