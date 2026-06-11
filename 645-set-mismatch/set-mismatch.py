class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = []
        s = set(nums)
        for x in s:
            if nums.count(x) == 2:
                m.append(x)     
        for i in xrange(1, len(nums) + 1):
            if i not in s:
                m.append(i)     
                break
        return m