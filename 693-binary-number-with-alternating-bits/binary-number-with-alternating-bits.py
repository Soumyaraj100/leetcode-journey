class Solution(object):
    def hasAlternatingBits(self, n):
        while n > 1:
            if (n & 1) == ((n >> 1) & 1):
                return False
            n = n >> 1
        return True