class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        m=[]
        for i in xrange(len(s.split())):
            m.append((s.split()[i])[::-1])
        x=" ".join(map(str,m))
        return x
