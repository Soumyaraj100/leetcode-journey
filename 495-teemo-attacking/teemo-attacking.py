class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            ans += min(duration, gap)
        return ans + duration