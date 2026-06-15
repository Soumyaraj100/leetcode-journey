class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s=[]
        for i in xrange(min(len(nums1),len(nums2))):
            if len(nums1)>=len(nums2):
                if nums2[i] in nums1:
                    s.append(nums2[i])
            elif len(nums1)<len(nums2):    
                if nums1[i] in nums2:    
                    s.append(nums1[i])
        return list(set(s))
            
            
                
