from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict

     #S = list(s)
       # T = list(t)
       # S.sort()
       # T.sort()
      #  if S == T:
       #     return True
       # else:
       #     return False '''
        
  


           