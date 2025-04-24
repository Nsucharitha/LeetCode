class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
       lis = s.split()
       ans = lis[:k]
       my_string = " ".join(ans)
       return my_string