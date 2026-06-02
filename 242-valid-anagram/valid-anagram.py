class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(s)):
                if len(s)!=len(t):
                    return False
                elif t.count(s[i]) != s.count(s[i]):
                    return False
        return True
