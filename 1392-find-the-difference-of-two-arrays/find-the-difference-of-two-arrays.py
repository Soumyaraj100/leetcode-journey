class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        n1=[]
        n2=[]
        s=[]
        for x in set(nums1):
            if x not in set(nums2):
                n1.append(x)
        for x in set(nums2):
            if x not in set(nums1):
                n2.append(x)
        s.append(n1)
        s.append(n2)
        return s