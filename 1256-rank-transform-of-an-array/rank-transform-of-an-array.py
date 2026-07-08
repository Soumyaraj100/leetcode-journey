class Solution(object):
    def arrayRankTransform(self, arr):
        s = sorted(set(arr))

        rank = {}
        for i, x in enumerate(s):
            rank[x] = i + 1
        ans = []
        for x in arr:
            ans.append(rank[x])
        return ans