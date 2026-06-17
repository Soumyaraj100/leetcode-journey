class Solution(object):
    def processStr(self, s, k):
        lengths = []
        length = 0

        # First pass: compute length after every operation
        for ch in s:
            lengths.append(length)

            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            else:          # '%'
                pass

        if k >= length:
            return '.'

        # Second pass: work backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev = lengths[i]

            if 'a' <= ch <= 'z':
                # This letter was appended
                if k == prev:
                    return ch

            elif ch == '#':
                k %= prev

            elif ch == '%':
                if prev > 0:
                    k = prev - 1 - k

            elif ch == '*':
                # Deleted one character.
                # Previous length = prev, current length = prev-1 (if prev>0)
                if prev > 0:
                    if k == prev - 1:
                        # This character was deleted and never appears.
                        return '.'

        return '.' ###copied