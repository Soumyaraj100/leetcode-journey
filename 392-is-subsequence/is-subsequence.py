class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        for y in t:
            if i < len(s) and s[i] == y:
                i += 1
        return i == len(s)