class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        m = [""] * numRows
        row = 0
        down = True
        for i in xrange(len(s)):
            m[row] += s[i]
            if row == numRows - 1:
                down = False
            elif row == 0:
                down = True
            if down:
                row += 1
            else:
                row -= 1
        return "".join(m)
