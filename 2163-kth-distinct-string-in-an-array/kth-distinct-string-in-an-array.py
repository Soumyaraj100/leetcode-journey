class Solution(object):
    def kthDistinct(self, arr, k):
        s = []
        for x in arr:
            if arr.count(x) == 1:
                s.append(x)
        if len(s) < k:
            return ""
        return s[k - 1]