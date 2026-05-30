class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(strs[0]) != 0:
                strs[0] = strs[0][:-1]
                if strs[0] == "":
                    return ""
        return strs[0]