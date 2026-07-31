class Solution(object):
    def hg(self, n):
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        if n < 0:
            return "-" + self.hg(-n)
        if n < 36:
            return chars[n]
        return self.hg(n // 36) + chars[n % 36]
    def concatHex36(self, n):
        x = hex(n * n)[2:] + self.hg(n * n * n)
        return x.upper()