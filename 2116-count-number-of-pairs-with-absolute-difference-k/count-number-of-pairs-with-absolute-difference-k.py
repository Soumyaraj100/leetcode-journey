class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        import itertools
        x = list(itertools.combinations(nums, 2))
        for y in x:
            if abs(y[0] - y[1]) == k:
                s += 1
        return s