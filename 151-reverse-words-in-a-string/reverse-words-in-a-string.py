class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        y = s.strip()
        x = y.split()
        m = x[::-1]
        n = " ".join(map(str, m))
        return n