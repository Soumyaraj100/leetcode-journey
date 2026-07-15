class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        c = 0
        s = Counter(nums)
        for num, freq in s.items():
            if freq % k == 0:
                c += num * freq
        return c