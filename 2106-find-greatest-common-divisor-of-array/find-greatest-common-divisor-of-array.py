class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math
        x= math.gcd(min(nums),max(nums))
        return x