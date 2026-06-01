class Solution(object):
    def runningSum(self, nums):
        m=[]
        i=len(nums)-1
        while i>=0:
            m.append(sum(nums))
            nums.pop(i)
            i=i-1
        m=m[::-1]
        return m
            
        