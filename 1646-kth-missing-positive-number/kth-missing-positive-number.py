class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        num = 1
        while True:
            if num not in arr:
                k -= 1
                if k == 0:
                    return num
            num += 1 