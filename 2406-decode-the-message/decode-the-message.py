class Solution(object):
    def decodeMessage(self, key, message):
        mp = {}
        ch = ord('a')
        for c in key:
            if c != ' ' and c not in mp:
                mp[c] = chr(ch)
                ch += 1
        ans = ""
        for c in message:
            if c == ' ':
                ans += ' '
            else:
                ans += mp[c]
        return ans