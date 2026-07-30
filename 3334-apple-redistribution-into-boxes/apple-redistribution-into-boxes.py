class Solution(object):
    def minimumBoxes(self, apple, capacity):
        s = sorted(capacity, reverse=True)
        total = sum(apple)
        m = 0
        c = 0
        for x in s:
            m += x
            c += 1
            if m >= total:
                return c