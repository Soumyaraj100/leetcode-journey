class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        transposed = list(map(list, zip(*matrix)))
        ans = []
        for row in matrix:
            mn = min(row)
            col = row.index(mn)
            if mn == max(transposed[col]):
                ans.append(mn)
        return ans