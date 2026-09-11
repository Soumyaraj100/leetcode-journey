class Solution(object):
    from itertools import permutations
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        result = set(permutations(digits, 3))
        c = 0
        for x in result:
            if x[0] != 0 and x[2] % 2 == 0:
                c += 1
        return c