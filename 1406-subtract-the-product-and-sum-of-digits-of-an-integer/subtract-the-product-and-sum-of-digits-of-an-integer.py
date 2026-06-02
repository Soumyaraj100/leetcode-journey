class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 1 <= len(str(n)) <= 100000:
            x=1
            for i in range(len(str(n))):
                x=x*int((str(n))[i])
            a=0
            for i in range(len(str(n))):
                a=a+int((str(n))[i])
            c=x-a
        return (c)