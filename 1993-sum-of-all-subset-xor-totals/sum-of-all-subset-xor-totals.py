class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from itertools import chain, combinations
        def get_all_subsets(iterable):
            s = list(iterable)
            return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
        m = 0
        for x in get_all_subsets(nums):
            xor = 0
            for y in x:
                xor ^= y
            m += xor
        return m