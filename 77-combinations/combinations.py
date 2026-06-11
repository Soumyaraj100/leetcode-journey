import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        m=[]
        for x in xrange(1,n+1):
            m.append(x)
        s=list(map(list, itertools.combinations(m,k)))
        return s