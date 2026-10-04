class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for val in range(len(digits)-1,-1,-1):
            if digits[val]<9:
                digits[val]+=1
                return digits
            digits[val]=0
        return [1]+digits