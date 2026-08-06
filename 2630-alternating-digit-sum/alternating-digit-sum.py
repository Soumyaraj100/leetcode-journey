class Solution(object):
    def alternateDigitSum(self, n):
        s = str(n)[::-1]
        x = 0
        k = 0
        for d in s:
            if k % 2 == 0:
                x += int(d)
            else:
                x -= int(d)
            k += 1
        return -x if len(s) % 2 == 0 else x