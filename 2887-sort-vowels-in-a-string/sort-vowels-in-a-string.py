class Solution(object):
    def sortVowels(self, s):
        vowels = "aeiouAEIOU"
        chars = list(s)
        pos = []
        vals = []
        for i, ch in enumerate(chars):
            if ch in vowels:
                pos.append(i)
                vals.append(ch)
        vals.sort()
        for i, ch in zip(pos, vals):
            chars[i] = ch
        return "".join(chars)