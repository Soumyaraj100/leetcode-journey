class Solution(object):
    def rearrangeString(self, s, x, y):
        if y > x:
            return ''.join(sorted(s, reverse=True))
        else:
            return ''.join(sorted(s))