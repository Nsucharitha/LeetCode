class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = 0
        for i in operations:
            if i == "--X" or i == "X--":
                n -= 1
            elif i == "X++" or i == "++X":
                n += 1
        return n