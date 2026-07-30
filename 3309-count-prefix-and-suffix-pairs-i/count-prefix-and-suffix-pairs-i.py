class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in xrange(len(words)):
            for j in xrange(i+1,len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    c+=1
        return c