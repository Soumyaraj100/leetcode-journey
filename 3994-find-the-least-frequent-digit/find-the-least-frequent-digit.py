from collections import Counter
class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = Counter(str(n))
        return int(min(cnt, key=lambda x: (cnt[x], int(x))))