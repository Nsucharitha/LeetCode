class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums)-1 #initialize the pointers
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]: #comparing squares
                res.append(nums[l] * nums[l])
                l += 1 #increment left pointer
            else:
                res.append(nums[r] * nums[r])
                r -= 1 #decrement right pointer
        return res[::-1]  #reverse 
        