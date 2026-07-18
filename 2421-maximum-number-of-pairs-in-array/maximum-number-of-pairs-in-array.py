class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=0
        d=0
        seen=[]
        for x in nums:
            if x not in seen:
                c+=nums.count(x)//2
                d+=nums.count(x)%2
                seen.append(x)
        return [c,d]