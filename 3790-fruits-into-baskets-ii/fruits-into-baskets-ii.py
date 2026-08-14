class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        used = [False] * len(baskets)
        ans = 0
        for fruit in fruits:
            for i in range(len(baskets)):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    break
            else:
                ans += 1
        return ans
