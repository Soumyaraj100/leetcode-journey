class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans = []
        for x in arr2:
            for y in arr1:
                if x == y:
                    ans.append(y)
        rem = []
        for x in arr1:
            if x not in arr2:
                rem.append(x)
        rem.sort()
        return ans + rem