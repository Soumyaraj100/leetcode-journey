class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s=[]
        import itertools
        c = ["".join(combo) for combo in itertools.product("10", repeat=n)]
        for x in c:
            if "00"  not in x:
                s.append(x)
        return s

