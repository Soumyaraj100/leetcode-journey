class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0
        n = len(arr)

        for i in xrange(n):
            for j in xrange(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:
                    for k in xrange(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1

        return count