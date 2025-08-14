class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in has:
                return [has[diff],i]

            has[n] = i

        return 
        