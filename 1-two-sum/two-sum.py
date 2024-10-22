class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if target == nums[i]+nums[j]:
                    return [i,j]

'''
Solution using Hashmap gives Time complexity as O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        h = {}
        for i in range(n):
            h[nums[i]] = i
        for j in range(n):
            y = target - nums[i]
            if y in h and h[y]!=i:
                return [i,h[y]]

'''
