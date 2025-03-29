class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return c.isalnum()

       
""" Brute force
        s = s.lower()
        new_s = "".join(filter(str.isalnum, s))
        rev_s = "".join(reversed(new_s))
        if new_s == rev_s:
            return True
        else:
            return False
            
sol 1:
This is like the bruteforce, here we use extra memory i.e new strings
new_s = ""
for c in s:
    if c.isalnum():
        new_s += c.lower()
    return new_s == new_s[::-1]"""
        