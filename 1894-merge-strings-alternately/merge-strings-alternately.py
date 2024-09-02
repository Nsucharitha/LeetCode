class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = []
        for i, j in zip(word1, word2):
            L.append(i + j)
        L.append(word1[len(word2):])
        L.append(word2[len(word1):])
        return "".join(L)
        

        