class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        temp = ""
        for x in words:
            temp += x
            if temp == s:
                return True
        return False