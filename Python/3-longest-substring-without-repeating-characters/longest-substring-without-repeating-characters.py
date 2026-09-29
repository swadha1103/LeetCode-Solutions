class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        l=''
        for ch1 in range(0,len(s)):
            chk=set()
            for ch2 in range(ch1,len(s)):
                if s[ch2] in chk:
                    break
                chk.add(s[ch2])
                if len(chk)>maxx:
                    maxx=len(chk)
                    l=s[ch1:ch2+1]
        return maxx