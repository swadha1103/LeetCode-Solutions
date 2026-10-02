class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
       ans=''
       for val in range(0,len(number)):
            if number[val]==digit:
                temp=number[:val]+number[val+1:]
                if temp>ans:
                    ans=temp
       return ans

        
        