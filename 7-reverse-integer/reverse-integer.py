class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        ans = 0

        while x:
            dig = x % 10
            ans = ans * 10 + dig
            x //= 10

        ans *= sign

        # Check 32-bit overflow
        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans

