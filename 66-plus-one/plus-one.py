class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum=0
        n=len(digits)
        for i in xrange(n):
            sum=sum+(digits[i]*(10**(n-i-1)))
        m=[int((str(sum+1))[i]) for i in xrange(len(str(sum+1)))]
        return m

