class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        setA = set()
        setB = set()
        ans = []
        for i in xrange(len(A)):
            setA.add(A[i])
            setB.add(B[i])
            ans.append(len(setA & setB))
        return ans