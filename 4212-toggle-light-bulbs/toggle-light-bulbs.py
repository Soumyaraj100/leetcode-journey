from collections import Counter
class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        c = Counter(bulbs)
        ans = []
        for bulb, cnt in c.items():
            if cnt % 2 == 1:
                ans.append(bulb)
        ans.sort()
        return ans