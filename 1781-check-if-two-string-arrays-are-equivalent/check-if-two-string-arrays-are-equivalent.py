class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1=word1[0]
        w2=word2[0]
        for i in xrange(1,len(word1)):
            w1=w1+word1[i]
        for i in xrange(1,len(word2)):
            w2=w2+word2[i]
        return w1==w2
            