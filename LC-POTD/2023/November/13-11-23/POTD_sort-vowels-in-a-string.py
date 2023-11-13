class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)

        result = []
        for char in s:
            if char.lower() in 'aeiou':
                result.append(vowels.pop())
            else:
                result.append(char)
        
        return ''.join(result)