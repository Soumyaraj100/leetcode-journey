class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        ans = 0
        for num in range(left, right + 1):
            if isPrime(bin(num).count("1")):
                ans += 1
        return ans