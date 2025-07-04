class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            a = 0
            while i:
                a += i%2
                i = i>>1
            res.append(a)

        return res
        