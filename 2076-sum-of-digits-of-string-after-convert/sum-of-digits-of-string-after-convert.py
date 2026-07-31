class Solution(object):
    def getLucky(self, s, k):
        c = ""
        for x in s:
            c += str(ord(x) - ord('a') + 1)
        c = int(c)
        while k > 0:
            total = 0
            while c != 0:
                total += c % 10
                c = c // 10
            c = total
            k -= 1
        return c