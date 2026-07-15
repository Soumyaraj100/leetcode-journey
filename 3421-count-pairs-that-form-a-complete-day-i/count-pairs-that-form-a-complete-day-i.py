class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        import itertools
        c = 0
        for x in itertools.combinations(hours, 2):
            if sum(x) % 24 == 0:
                c += 1
        return c