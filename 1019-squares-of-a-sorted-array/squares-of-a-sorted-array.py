
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = [ele*ele for ele in nums]
        squares.sort()
        return squares