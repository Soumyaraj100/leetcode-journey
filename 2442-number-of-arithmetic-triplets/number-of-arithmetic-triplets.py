class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        s=0
        for i in xrange(len(nums)):
            for j in xrange(i+1,len(nums)):
                for k in xrange(j+1,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        s+=1
        return s