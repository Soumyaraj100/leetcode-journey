class Solution(object):
    def decompressRLElist(self, nums):
        s = []
        for i in xrange(0, len(nums), 2):
            freq = nums[i]
            while freq > 0:
                s.append(nums[i+1])
                freq -= 1
        return s