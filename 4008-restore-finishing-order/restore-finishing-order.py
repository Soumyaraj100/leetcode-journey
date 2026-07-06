class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        s=[]
        for x in order:
            if x in friends:
                s.append(x)
        return s