class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=list(set(list(s)))
        vowels=["a","e","i","o","u"]
        v=[]
        c=[]
        for m in x:
            if m in vowels:
                v.append(s.count(m))
            else:
                c.append(s.count(m))
        if v and c:
            return max(v)+max(c)
        elif v:
            return max(v)
        else:
            return max(c)