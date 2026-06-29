class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count=0
        for x in patterns:
            if x in word:
                count+=1
        return count