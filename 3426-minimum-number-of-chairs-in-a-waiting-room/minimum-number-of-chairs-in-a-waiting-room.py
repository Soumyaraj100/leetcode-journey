class Solution(object):
    def minimumChairs(self, s):
        c = 0
        ans = []
        for x in s:
            if x == "E":
                c += 1
                ans.append(c)
            elif x == "L":
                c -= 1
                ans.append(c)
        return max(ans)