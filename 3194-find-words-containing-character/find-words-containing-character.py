class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        m=[]
        for i in xrange(len(words)):
            if words[i].count(x)!=0:
                m.append(i)
        return m