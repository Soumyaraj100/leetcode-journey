class Solution(object):
    def permuteUnique(self, nums):
        import itertools
        permutations_tuples = set(itertools.permutations(nums))
        return [list(p) for p in permutations_tuples]