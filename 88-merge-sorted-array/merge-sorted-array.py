class Solution(object):
    def merge(self, nums1, m, nums2, n):
        j = nums1[:m] + nums2
        j.sort()
        nums1[:] = j