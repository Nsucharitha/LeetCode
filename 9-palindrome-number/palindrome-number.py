class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            n = x
            rev = 0
            dig = 0
            while (x > 0):
                dig = x % 10
                rev = rev * 10 + dig
                x = x // 10
            if n == rev:
                return True
            else:
                return False
        