class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines = 1
        curr = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if curr + w > 100:
                lines += 1
                curr = w
            else:
                curr += w
        return [lines, curr]