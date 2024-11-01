class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        c = 0
        for i in stones:
            if i in s:
                c += 1
        return c
        