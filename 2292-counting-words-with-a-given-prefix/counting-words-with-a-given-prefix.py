class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        s=0
        for x in words:
            if x.startswith(pref):
                s+=1
        return s