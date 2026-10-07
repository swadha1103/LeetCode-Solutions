class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while i>=0:
            if nums[i]<nums[i+1]:
                break
            i-=1
        if i==-1:
            nums.reverse()
            return
        grt=None
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i] and (grt is None or nums[j]<nums[grt]):
                grt=j
        nums[i],nums[grt]=nums[grt],nums[i]
        nums[i+1:]=sorted(nums[i+1:])
        