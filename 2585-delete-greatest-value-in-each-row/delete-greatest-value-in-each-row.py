class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s=0
        for row in grid:
            row.sort()
        for j in xrange(len(grid[0])):
            s+=max(row.pop() for row in grid)
        return s
