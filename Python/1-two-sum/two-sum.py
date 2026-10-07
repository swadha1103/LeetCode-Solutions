class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for v1 in range(0,len(nums)):
            for v2 in range(v1+1,len(nums)):
                if nums[v1]+nums[v2]==target:
                    return v1,v2
        