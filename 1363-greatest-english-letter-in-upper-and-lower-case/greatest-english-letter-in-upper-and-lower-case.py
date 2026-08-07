class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for x in s:
            if x.isupper() and x.lower() in s:
                res.append(x)
            elif x.islower() and x.upper() in s:
                res.append(x.upper())
        res.sort()
        if res:
            return res[-1]
        return ""