class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        count = 0
        for battery in batteryPercentages:
            if battery > count:
                count += 1
        return count