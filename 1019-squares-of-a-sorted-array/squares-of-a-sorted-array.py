class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in nums:
            new_nums.append(i*i)
        new_nums.sort()
        return new_nums
        