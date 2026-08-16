class Solution(object):
    def reformat(self, s):
        letters = []
        digits = []
        for x in s:
            if x.isalpha():
                letters.append(x)
            else:
                digits.append(x)
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) < len(digits):
            letters, digits = digits, letters
        res = ""
        for i in range(len(digits)):
            res += letters[i] + digits[i]
        if len(letters) > len(digits):
            res += letters[-1]
        return res