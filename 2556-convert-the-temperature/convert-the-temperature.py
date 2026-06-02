class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        if 0 <= celsius <= 1000:
            s=[(celsius + 273.15),(celsius * 1.80 + 32.00)]
        return s