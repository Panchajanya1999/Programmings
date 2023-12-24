class Solution:
    def minOperations(self, s: str) -> int:
        s1, s2 = '', ''
        for i in range(len(s)):
            if i % 2 == 0:
                s1 += '0'
                s2 += '1'
            else:
                s1 += '1'
                s2 += '0'
        
        diff1 = sum(c1 != c2 for c1, c2 in zip(s, s1))
        diff2 = sum(c1 != c2 for c1, c2 in zip(s, s2))
        
        return min(diff1, diff2)
