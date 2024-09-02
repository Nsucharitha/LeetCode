class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = ""
        for i in range(min(len(word1),len(word2))):
            L = L + word1[i] + word2[i]
        if len(word1) < len(word2):
            L = L + word2[len(word1):]
        else:
            L = L + word1[len(word2):]
        return L
        

        