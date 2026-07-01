class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s) > 2:
            m = ""
            for i in xrange(len(s) - 1):
                m += str((int(s[i]) + int(s[i + 1])) % 10)
            s = m
        return s[0] == s[1]