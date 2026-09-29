class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for v1 in range(0,len(nums)):
            for v2 in range(v1+1,len(nums)):
                if nums[v1]+ nums[v2]==target:
                    return v1,v2