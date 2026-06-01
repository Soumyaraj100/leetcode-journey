class Solution(object):
    def shuffle(self, nums, n):
        m=[]
        for i in range(n):
            m.append(nums[i])
            m.append(nums[n+i])
        return m