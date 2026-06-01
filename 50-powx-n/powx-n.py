class Solution(object):
    def myPow(self, x, n):
        if -100.0 < x < 100.0 and -231 <= n <= 231-1 and x!=0 or n!=0:
            t=pow(x,n)
        return t
        