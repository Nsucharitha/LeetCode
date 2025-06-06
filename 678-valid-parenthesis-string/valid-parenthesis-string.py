class Solution:
    def checkValidString(self, s: str) -> bool:
        min = 0
        max = 0
        for i in range(len(s)):
            if s[i] == '(':
                min += 1
                max += 1
            elif s[i] == ')':
                min -= 1
                max -= 1
            else:
                min -= 1
                max += 1
            if min <0:
                min = 0
            if max <0:
                return False
        return (min ==0)
                
"""
        n = len(s)
        def func(s, indx, count):
            if count < 0:
                return False
            if indx ==n:
                return (count==0)
            if s[indx] == '(':
                return func(s, indx+1, count+1)
            if s[indx] == ')':
                return func(s, indx+1, count-1)
            else:
                return func(s, indx+1, count+1) or func(s, indx+1, count-1) or func(s, indx+1,count)

        return func(s,0,0) 
"""