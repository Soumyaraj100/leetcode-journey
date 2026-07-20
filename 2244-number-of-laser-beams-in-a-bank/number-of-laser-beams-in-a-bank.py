class Solution(object):
    def numberOfBeams(self, bank):
        m = []
        for row in bank:
            cnt = row.count("1")
            if cnt != 0:
                m.append(cnt)
        c = 0
        for i in xrange(len(m) - 1):
            c += m[i] * m[i + 1]
        return c