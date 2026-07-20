class Solution(object):
    def findDifferentBinaryString(self, nums):
        ans = ""
        for i in xrange(len(nums)):
            if nums[i][i] == '0':
                ans += '1'
            else:
                ans += '0'
        return ans