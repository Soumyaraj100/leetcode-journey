class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alphabets = "qwertyuiopasdfghjklzxcvbnm"
        for a in alphabets:
            if s.count(a)!=t.count(a):
                return False
        return True
