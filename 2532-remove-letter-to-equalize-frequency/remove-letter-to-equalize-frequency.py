from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        c = Counter(word)
        for ch in c:
            c[ch] -= 1
            if c[ch] == 0:
                del c[ch]
            if len(set(c.values())) == 1:
                return True
            c[ch] += 1
        return False