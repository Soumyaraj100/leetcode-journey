class Solution(object):
    def minElement(self, nums):
        result = []
        n = len(nums)

        for i in range(n):
            temp = list(str(nums[i]))
            add = 0

            for j in range(len(temp)):
                add = add + int(temp[j])

            result.append(add)

        mini = min(result)
        return(mini)