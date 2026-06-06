class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum=[0]
        rightsum=[0]
        ans=[]
        sum=0
        for i in xrange(1,len(nums)):
            sum=sum+nums[i-1]
            leftsum.append(sum)     
        rnums=nums[::-1]  
        sum=0    
        for i in xrange(1,len(nums)):
            sum=sum+rnums[i-1]
            rightsum.append(sum) 
        rightsum.reverse()
        for i in xrange(len(nums)):
            ans.append(abs(leftsum[i]-rightsum[i]))  
        return ans