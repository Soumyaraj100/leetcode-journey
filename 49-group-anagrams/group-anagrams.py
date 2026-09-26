class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for x in strs:
            key = ''.join(sorted(x))
            if key not in res:
                res[key] = []
            res[key].append(x)
        return list(res.values())