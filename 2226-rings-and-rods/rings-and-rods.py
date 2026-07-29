class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        h = {}
        for i in xrange(0, len(rings), 2):
            rod = int(rings[i+1])
            color = rings[i]
            if rod not in h:
                h[rod] = set()
            h[rod].add(color)
        count = 0
        for colors in h.values():
            if len(colors) == 3:
                count += 1
        return count
