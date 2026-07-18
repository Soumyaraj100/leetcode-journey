class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        s=0
        c=0
        for x in events:
            if x=="W":
                c+=1
                if c == 10:
                    break
            elif x=="WD" or x=="NB":
                s+=1
            else:
                s+=int(x)
        return [s,c]