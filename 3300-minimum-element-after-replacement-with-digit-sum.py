nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
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
        print(mini)
obj = Solution()
obj.minElement(nums)
#in leetcode nums must be written in the code  itself cause input doesnt work on leetcode
#line 17 and 18 should be removed cause leetcode calls the program automatically