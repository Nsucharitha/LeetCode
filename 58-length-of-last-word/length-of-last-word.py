class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split()
        res = len(new[-1])

        return res
        