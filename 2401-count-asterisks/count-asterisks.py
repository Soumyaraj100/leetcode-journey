class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        y=0
        for m in s:
            if m=="|":
                x+=1
            if m=="*" and x%2==0:
                y+=1
        return y
                