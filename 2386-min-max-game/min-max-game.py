class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        k = 0
        while k < len(nums):
            if k % 4 == 0:
                temp.append(min(nums[k:k+2]))
            else:
                temp.append(max(nums[k:k+2]))
            k += 2
        if len(temp) == 1:
            return temp[0]
        return self.minMaxGame(temp)