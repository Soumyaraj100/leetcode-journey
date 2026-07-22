class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        n = len(piles) // 3
        ans = 0
        for i in xrange(n):
            ans += piles[2*i + 1]
        return ans