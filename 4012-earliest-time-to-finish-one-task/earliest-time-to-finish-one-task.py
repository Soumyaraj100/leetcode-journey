class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        s=[]
        for x in tasks:
            s.append(sum(x))
        return min(s)