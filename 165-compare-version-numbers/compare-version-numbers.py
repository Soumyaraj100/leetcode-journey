class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        n = max(len(v1), len(v2))
        for i in range(n):
            x = int(v1[i]) if i < len(v1) else 0
            y = int(v2[i]) if i < len(v2) else 0
            if x < y:
                return -1
            elif x > y:
                return 1
        return 0