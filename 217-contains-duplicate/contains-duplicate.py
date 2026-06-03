class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numb=set(nums)
        m=len(list(numb))
        if len(nums)!=m:
            return True
        else:
            return False