class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if 1 <= len(haystack) <= 10000 and 1 <= len(needle) <=10000:
            return(haystack.find(needle))
        