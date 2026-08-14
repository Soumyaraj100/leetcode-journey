class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        prev = 0
        for i in xrange(len(releaseTimes)):
            x = releaseTimes[i]
            releaseTimes[i] = releaseTimes[i] - prev
            prev = x
        m = max(releaseTimes)
        ans = keysPressed[releaseTimes.index(m)]
        for i in xrange(len(releaseTimes)):
            if releaseTimes[i] == m:
                ans = max(ans, keysPressed[i])
        return ans