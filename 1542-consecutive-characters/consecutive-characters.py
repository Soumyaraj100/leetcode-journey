class Solution(object):
    def maxPower(self, s):
        m = [s[0]]
        n = 1
        for x in s[1:]:
            if x == m[-1]:
                m.append(x)
            else:
                n = max(n, len(m))
                m = [x]
        n = max(n, len(m))
        return n