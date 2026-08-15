class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        count = {}
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            key = (a, b)
            if key in count:
                ans += count[key]
            count[key] = count.get(key, 0) + 1
        return ans