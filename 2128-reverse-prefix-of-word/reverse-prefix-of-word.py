class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        x = word.find(ch)
        if x == -1:
            return word
        return word[:x+1][::-1] + word[x+1:]