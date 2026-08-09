class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones)>1:
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(x - y)
            stones.sort()
        if stones:
            return stones[0]
        return 0