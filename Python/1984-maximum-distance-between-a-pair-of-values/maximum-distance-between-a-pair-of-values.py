class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        #brute force
        '''maxx=0
        diff=0
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if i<=j and nums1[i]<=nums2[j]:
                    diff=j-i
            if diff>maxx:
                maxx=diff
        return maxx'''


        maxx=0
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                maxx=max(maxx,j-i)
                j+=1
            else:
                i+=1
        return maxx
        