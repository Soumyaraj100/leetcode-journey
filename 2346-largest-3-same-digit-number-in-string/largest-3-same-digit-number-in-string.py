class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        s=["000","111", "222", "333", "444", "555", "666", "777", "888", "999"]
        ans=[]
        for x in s:
            if x in num:
                ans.append(x)
        if ans:
            return max(ans)
        else:
            return ""