class Solution:
    def maxDifference(self, s: str) -> int:
        dic={}
        odd=0
        even=float(inf)
        for ch in s:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1
        for ch in dic:
            if dic[ch]%2!=0:
                if dic[ch]>odd:
                    odd=dic[ch]
            else:
                if dic[ch]<even:                   
                   even=dic[ch]
        return odd-even
