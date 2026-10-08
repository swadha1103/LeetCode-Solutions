class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff=0
        maxx=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i<j and nums[i]<nums[j]:
                    diff =nums[j]-nums[i]
                    if diff>maxx:
                        maxx=diff
        if maxx==0:
            return -1
        return maxx