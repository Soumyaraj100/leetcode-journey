class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for ch in set(words[0]):
            mini = words[0].count(ch)
            for i in xrange(1, len(words)):
                mini = min(mini, words[i].count(ch))
            ans.extend([ch] * mini)
        return ans