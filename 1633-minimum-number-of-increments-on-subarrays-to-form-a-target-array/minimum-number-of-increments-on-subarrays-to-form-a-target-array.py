class Solution(object):
    def minNumberOperations(self, target):
        c = target[0]
        for i in xrange(1, len(target)):
            if target[i] > target[i-1]:
                c += target[i] - target[i-1]
        return c