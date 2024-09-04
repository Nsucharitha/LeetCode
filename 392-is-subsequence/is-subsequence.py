class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)
        if a == 0:
            return True
        if a>b:
            return False
        j = 0
        for i in range(b):
            if t[i] == s[j]:
                if j == a-1:
                    return True
                j += 1
        return False
        