class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=[]
        n=bin(n)
        m=0
        for i in xrange(len(n)):
            if n[i]=="1":
                s.append(i)
        if len(s)==1:
            return 0
        for i in xrange(len(s)-1):
            m=max(m,abs(s[i]-s[i+1]))
        return m