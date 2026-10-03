class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        c=0
        for v1 in range(len(startTime)):
            if startTime[v1]<=queryTime<=endTime[v1]:
                c=c+1
        return c
