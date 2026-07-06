class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        from collections import Counter
        x = Counter(str(n))
        for m, n in x.items():
            s += int(m) * n
        return s