class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s=0
        for x in grid:
            for y in x:
                if y<0:
                    s+=1
        return s