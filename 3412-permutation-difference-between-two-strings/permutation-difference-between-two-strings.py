class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        pos = {}
        for i in xrange(len(s)):
            pos[s[i]] = i
        ans = 0
        for i in xrange(len(t)):
            ans += abs(pos[t[i]] - i)
        return ans