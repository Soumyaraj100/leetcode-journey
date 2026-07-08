class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        from collections import Counter
        char_count = Counter(chars)
        ans = 0
        for word in words:
            word_count = Counter(word)
            good = True
            for ch in word_count:
                if word_count[ch] > char_count[ch]:
                    good = False
                    break
            if good:
                ans += len(word)
        return ans