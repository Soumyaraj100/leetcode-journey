class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        s=startTime.split(":")
        e=endTime.split(":")
        st=int(s[0])*3600+int(s[1])*60+int(s[2])
        et=int(e[0])*3600+int(e[1])*60+int(e[2])
        return et-st