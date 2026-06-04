class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        m=0
        for x in range(num1,num2+1):
            x=str(x)
            for i in xrange(len(x)):
                if i!=0 and i!=(len(str(x))-1):
                    if x[i-1]<x[i]>x[i+1] or x[i-1]>x[i]<x[i+1] :
                        m=m+1
                else:
                    m=m+0
        return m


