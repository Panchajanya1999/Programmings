class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        s2 = ""

        for s in word1:
            s1 += s
        for s in word2:
            s2 += s
        
        return s1 == s2
        
