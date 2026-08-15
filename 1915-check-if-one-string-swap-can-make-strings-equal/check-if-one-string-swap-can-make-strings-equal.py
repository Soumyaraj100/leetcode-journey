class Solution(object):
    def areAlmostEqual(self, s1, s2):
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        if len(diff) == 0:
            return True
        if len(diff) != 2:
            return False
        a = diff[0]
        b = diff[1]
        return s1[a] == s2[b] and s1[b] == s2[a]