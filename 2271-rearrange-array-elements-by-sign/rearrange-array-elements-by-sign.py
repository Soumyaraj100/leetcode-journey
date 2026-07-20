class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        n=[]
        s=[]
        for x in nums:
            if x>0:
                p.append(x)
            else:
                n.append(x)
        for i in xrange(len(p)):
            s.append(p[i])
            s.append(n[i])
        return s
            