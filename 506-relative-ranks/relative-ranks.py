class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        res=sorted(score,reverse=True)
        ans=[]
        for x in score:
            if res.index(x)==0:
                ans.append("Gold Medal")
            elif res.index(x)==1:
                ans.append("Silver Medal")
            elif res.index(x)==2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(res.index(x)+1))
        return ans