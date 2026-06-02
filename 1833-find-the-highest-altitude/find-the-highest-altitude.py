class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        pa=0
        alt=[0]
        for i in xrange(len(gain)):
            na=pa+gain[i]
            alt.append(na)
            pa=na
        return max(alt)