class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candies = max(candies)
        for i in candies:
            ans.append(i + extraCandies >= max_candies)
        return ans
        