class Solution(object):
    def runningSum(self, nums):
        s = 0
        m = []
        for x in nums:
            s += x
            m.append(s)
        return m