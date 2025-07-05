class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        # Count frequency of each number
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        lucky = -1
        # Check for lucky numbers
        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky
