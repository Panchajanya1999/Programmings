class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left_zeros = 0
        right_ones = s.count('1')
        
        for i in range(1, len(s)):
            if s[i-1] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        
        return max_score
