class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1,1
        for i in nums:
            if i ==0:
                curMin, curMax = 1,1
                continue
            tmp = curMax * i
            curMax = max(i * curMax, i*curMin, i)
            curMin = min(tmp, i*curMin, i)
            res = max(res, curMax)

        return res

        