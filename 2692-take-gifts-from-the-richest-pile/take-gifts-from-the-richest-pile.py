class Solution(object):
    def pickGifts(self, gifts, k):
        for i in xrange(k):
            gifts.sort(reverse=True)
            gifts[0] = int(gifts[0] ** 0.5)
        return sum(gifts)