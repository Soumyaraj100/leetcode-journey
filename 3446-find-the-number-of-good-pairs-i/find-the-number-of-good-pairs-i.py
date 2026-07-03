class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for x in nums1:
            for y in nums2:
                if x%(y*k)==0:
                    c+=1
        return c