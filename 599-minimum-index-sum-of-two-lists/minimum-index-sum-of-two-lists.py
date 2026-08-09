class Solution(object):
    def findRestaurant(self, list1, list2):
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        ans = []
        min_sum = float('inf')
        for j in range(len(list2)):
            if list2[j] in d:
                total = d[list2[j]] + j
                if total < min_sum:
                    min_sum = total
                    ans = [list2[j]]
                elif total == min_sum:
                    ans.append(list2[j])
        return ans