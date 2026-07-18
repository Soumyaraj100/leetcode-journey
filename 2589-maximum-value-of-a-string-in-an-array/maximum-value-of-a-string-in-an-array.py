class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        s=[]
        for x in strs:
            if x.isdigit():
                s.append(int(x))
            else:
                s.append(len(x))
        return max(s)