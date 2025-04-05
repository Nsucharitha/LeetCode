class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n-1) not in numSet:
                next_num = n+1
                length = 1
                while next_num in numSet:
                    length += 1
                    next_num += 1
                longest = max(length, longest)
        return longest        