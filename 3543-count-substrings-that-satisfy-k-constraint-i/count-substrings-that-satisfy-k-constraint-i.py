class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        c = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                if sub.count("0") <= k or sub.count("1") <= k:
                    c += 1
        return c