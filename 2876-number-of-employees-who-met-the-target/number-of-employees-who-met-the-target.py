class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        for x in hours:
            if x>=target:
                s=s+1
        return s