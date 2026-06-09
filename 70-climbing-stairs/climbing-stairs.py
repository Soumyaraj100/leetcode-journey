import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        a, b = 1, 2
        for i in xrange(3, n + 1):
            a, b = b, a + b
        return b