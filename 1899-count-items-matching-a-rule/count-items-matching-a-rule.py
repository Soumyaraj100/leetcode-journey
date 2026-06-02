class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        k = 0

        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2

        for i in range(len(items)):
            if items[i][idx] == ruleValue:
                k += 1

        return k                