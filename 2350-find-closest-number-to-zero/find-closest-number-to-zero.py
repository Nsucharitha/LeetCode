class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        L = []
        for i in nums:
           L.append(abs(i))
        L.sort()
        if L[0] in nums:
            return L[0]
        else:
            return -abs(L[0])