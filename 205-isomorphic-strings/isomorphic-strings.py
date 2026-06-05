class Solution(object):
    def isIsomorphic(self, s, t):
        a = []
        b = []
        for ch in s:
            a.append(s.index(ch))
        for ch in t:
            b.append(t.index(ch))
        return a == b