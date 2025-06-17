class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        temp = str(num)
        n = len(temp)
        l = 0
        r = k-1
        summ = 0
        while r < n:
            arr = temp[l:r+1]
            if int(arr) != 0 and num % int(arr) == 0:
                summ += 1

            l += 1
            r += 1

        return summ
        