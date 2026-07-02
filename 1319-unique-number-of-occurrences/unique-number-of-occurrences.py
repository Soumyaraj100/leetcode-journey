class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        x=dict(Counter(arr))
        return len(x) == len(set(x.values()))
