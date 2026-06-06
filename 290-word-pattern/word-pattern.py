class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        m=[]
        n=[]
        l=s.split()
        while len(pattern)==len(l):
            for i in xrange(len(pattern)):
                m.append(pattern.index(pattern[i]))
            for i in xrange(len(pattern)):
                n.append(l.index(l[i]))
            return m==n
        if len(pattern) != len(l):
            return False
