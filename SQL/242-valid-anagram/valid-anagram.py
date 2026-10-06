class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for ch in s:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1
        for ch in t:
            if ch in dic:
                dic[ch]-=1
            else:
                print('False')
        for val in dic.values():
            if val!=0:
                return False
        return True