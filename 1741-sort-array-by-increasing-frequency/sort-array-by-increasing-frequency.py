class Solution(object):
    def frequencySort(self, nums):
        from collections import Counter
        x = Counter(nums)
        return sorted(nums, key=lambda n: (x[n], -n))