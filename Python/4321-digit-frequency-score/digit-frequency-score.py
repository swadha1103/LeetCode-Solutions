class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dic={}
        s=0
        while n>0:
            rem=n%10
            if rem in dic:
                dic[rem]+=1
            else:
                dic[rem]=1
            n=n//10
        for val in dic:
            s=s+val*dic[val]
        return s