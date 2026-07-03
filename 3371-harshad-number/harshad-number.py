class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        m=x
        while x:
            s+=x%10
            x=x//10
        if m%s==0:
            return s
        else:
            return -1