class Solution(object):
    def stringMatching(self, words):
        x = []
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if i != j and words[i] in words[j]:
                    x.append(words[i])
                    break
        return x