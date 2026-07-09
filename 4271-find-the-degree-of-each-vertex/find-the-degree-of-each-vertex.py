class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        s=[]
        for x in matrix:
            s.append(sum(x))
        return s