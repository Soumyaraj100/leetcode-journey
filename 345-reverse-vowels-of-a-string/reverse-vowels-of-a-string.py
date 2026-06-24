class Solution(object): 
    def reverseVowels(self, s): 
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        m = []
        for x in s:
            if x in vowels:
                m.append(x)
        m.reverse()
        s = list(s)
        k = 0
        for i in xrange(len(s)):
            if s[i] in vowels:
                s[i] = m[k]
                k += 1
        return "".join(s)