class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            for part in word.split(separator):
                if part:
                    ans.append(part)
        return ans
        