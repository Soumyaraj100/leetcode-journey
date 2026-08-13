class Solution(object):
    def secondHighest(self, s):
        res = []
        for x in s:
            if x.isdigit():
                res.append(int(x))
        res = set(res)
        res = sorted(res)
        if len(res) < 2:
            return -1
        return res[-2]