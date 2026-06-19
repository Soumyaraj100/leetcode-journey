class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        l=[]
        r=[]
        e=[]
        for i in xrange(len(nums)):
            if nums[i]<pivot:
                l.append(nums[i])
            elif nums[i]>pivot:
                r.append(nums[i])
            else:
                e.append(nums[i])
        return(l+e+r)     