class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=[]
        for x in nums1:
            for y in nums2:
                if x == y:
                    s.append(x)
                    nums2.remove(y)
                    break
        return s