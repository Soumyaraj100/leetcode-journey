class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        permutations_tuples = itertools.permutations(nums)
        return [list(p) for p in permutations_tuples]