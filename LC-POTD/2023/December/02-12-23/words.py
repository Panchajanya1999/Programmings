class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = 0
        for word in words:
            flag = True
            for c in word:
                if word.count(c) > chars.count(c):
                    flag = False
                    break
            if flag:
                cnt += len(word)
        return cnt
