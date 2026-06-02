class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        c=0
        if 1 <= len(jewels) <= 50 and 1 <= len(stones) <= 50 and jewels.isalpha() and stones.isalpha() :
            for i in xrange(len(jewels)):
                c=c+stones.count(jewels[i])
            return c