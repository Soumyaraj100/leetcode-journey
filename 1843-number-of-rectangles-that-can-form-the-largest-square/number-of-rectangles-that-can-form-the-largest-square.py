class Solution(object):
    def countGoodRectangles(self, rectangles):
        m = 0
        count = 0
        for x in rectangles:
            if min(x) > m:
                m = min(x)
                count = 1
            elif min(x) == m:
                count += 1
        return count