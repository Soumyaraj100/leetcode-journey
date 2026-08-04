class Solution(object):
    def countEven(self, num):
        s = 0
        x = num
        while num:
            s += num % 10
            num //= 10
        ans = x // 2
        if s % 2 == 1 and x % 2 == 0:
            ans -= 1
        return ans