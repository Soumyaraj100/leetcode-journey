class Solution(object):
    def minCosts(self, cost):
        ans = []
        mn = float('inf')
        for c in cost:
            mn = min(mn, c)
            ans.append(mn)
        return ans