class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=''
        for ch1 in range(0,len(s)):
            for ch2 in range(ch1+1,len(s)+1):
                x=s[ch1:ch2+1]
                if x==x[::-1]:
                    if len(x)>len(l):
                        l=x
        return l

        