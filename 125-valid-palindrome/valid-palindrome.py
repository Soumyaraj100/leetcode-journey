class Solution(object):
    def isPalindrome(self, s):
        q = ""
        for ch in s.lower():
            if ch.isalnum():
                q += ch
        return q == q[::-1]