class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        m=0
        for x in s:
            if x=="R":
                c+=1
            else:
                c-=1
            if c==0:
                m+=1
        return m