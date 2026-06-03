class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if 1 <= len(s) <= 10000:
            m=s.split()
            return(len(m[len(m)-1]))