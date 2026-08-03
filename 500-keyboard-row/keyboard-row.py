class Solution(object):
    def findWords(self, words):
        d = {}
        for ch in "qwertyuiop":
            d[ch] = 1
        for ch in "asdfghjkl":
            d[ch] = 2
        for ch in "zxcvbnm":
            d[ch] = 3
        ans = []
        for word in words:
            row = d[word[0].lower()]
            ok = True
            for ch in word.lower():
                if d[ch] != row:
                    ok = False
                    break
            if ok:
                ans.append(word)
        return ans