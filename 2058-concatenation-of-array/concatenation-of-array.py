class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = 0
        while n < 2:
            for i in nums:
                ans.append(i)

            n += 1

        return ans

        