class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s=[]
        for x in s1.split():
            if (s1.split()).count(x)==1 and x not in s2.split():
                s.append(x)
        for x in s2.split():
            if (s2.split()).count(x)==1 and x not in s1.split():
                s.append(x)
        return s