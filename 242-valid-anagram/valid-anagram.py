class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = list(s)
        T = list(t)
        S.sort()
        T.sort()
        if S == T:
            return True
        else:
            return False
           