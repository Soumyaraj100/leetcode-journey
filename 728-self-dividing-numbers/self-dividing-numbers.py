class Solution(object):
    def selfDividingNumbers(self, left, right):
        s = []
        for x in xrange(left, right + 1):
            ok = True
            for y in str(x):
                if y == '0' or x % int(y) != 0:
                    ok = False
                    break
            if ok:
                s.append(x)
        return s