class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        nums = []
        ans = []

        for row in grid:
            nums.extend(row)
        for x in nums:
            if nums.count(x) == 2:
                ans.append(x)
                break
        for i in xrange(1, len(nums) + 1):
            if i not in nums:
                ans.append(i)
                break

        return ans