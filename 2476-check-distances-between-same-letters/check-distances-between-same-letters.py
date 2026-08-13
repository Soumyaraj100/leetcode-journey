class Solution(object):
    def checkDistances(self, s, distance):
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i - 1 != distance[ord(s[i]) - ord('a')]:
                        return False
                    break
        return True