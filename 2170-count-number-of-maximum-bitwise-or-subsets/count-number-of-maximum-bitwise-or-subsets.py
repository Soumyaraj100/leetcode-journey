from itertools import combinations
class Solution(object):
    def get_subsets(self, nums):
        subsets = []
        for i in range(len(nums) + 1):
            for comp in combinations(nums, i):
                subsets.append(list(comp))
        return subsets
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subsets = self.get_subsets(nums)
        ans = []
        for x in subsets:
            cur = 0
            for y in x:
                cur |= y
            ans.append(cur)
        return ans.count(max(ans))