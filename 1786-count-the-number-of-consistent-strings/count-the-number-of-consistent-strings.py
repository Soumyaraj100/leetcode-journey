class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        s=0
        for x in words:
            if set(allowed)&set(x)==set(x):
                s+=1
        return s