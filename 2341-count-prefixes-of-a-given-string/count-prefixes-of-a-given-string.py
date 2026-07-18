class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        c=0
        for x in words:
            if s.startswith(x):
                c+=1
        return c