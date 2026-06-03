class Solution(object):
    def mostWordsFound(self, sentences):
        m=[]
        for i in xrange(len(sentences)):
            m.append(len(sentences[i].split()))
        return max(m)