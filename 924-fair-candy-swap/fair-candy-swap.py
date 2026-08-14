class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        a = sum(aliceSizes)
        b = sum(bobSizes)
        diff = (a - b) // 2
        bob = set(bobSizes)
        for x in aliceSizes:
            y = x - diff
            if y in bob:
                return [x, y]