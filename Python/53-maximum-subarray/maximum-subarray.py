class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
       cs=nums[0]
       ms=nums[0]
       for v1 in range(1,len(nums)):
        cs=max(nums[v1],nums[v1]+cs)
        ms=max(cs,ms)
       return ms


        