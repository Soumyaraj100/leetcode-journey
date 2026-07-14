from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_freq = max(freq.values())
        total = 0
        for v in freq.values():
            if v == max_freq:
                total += v
        return total