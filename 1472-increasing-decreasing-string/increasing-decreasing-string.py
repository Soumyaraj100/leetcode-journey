class Solution(object):
    def sortString(self, s):
        ans = ""
        while s:
            x = sorted(set(s))
            for ch in x:
                ans += ch
                s = s.replace(ch, "", 1)
            if not s:
                break
            x = sorted(set(s))
            for ch in x[::-1]:
                ans += ch
                s = s.replace(ch, "", 1)
        return ans