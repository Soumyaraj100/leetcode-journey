class Solution(object):
    def helper(self,x):
        s=list(str(x))
        p=max(s)*len(s)
        return int(p)
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for x in nums:
            ans.append(self.helper(x))
        return sum(ans)
    