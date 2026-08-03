class Solution(object):
    def countWords(self, words1, words2):
        d1 = {}
        d2 = {}
        for word in words1:
            d1[word] = d1.get(word, 0) + 1
        for word in words2:
            d2[word] = d2.get(word, 0) + 1
        count = 0
        for word in d1:
            if d1[word] == 1 and d2.get(word, 0) == 1:
                count += 1
        return count