class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in xrange(len(s)):
            if s[i].isdigit():
                s[i] = chr(ord(s[i-1]) + int(s[i]))
        return "".join(s)