# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 6, 2023
# Integer Break
# Link - https://leetcode.com/problems/integer-break/description/?envType=daily-question&envId=2023-10-06

class Solution:
    def integerBreak(self, n: int) -> int:
        # If n is less than or equal to 3, return n-1
        if 1 < n and n <= 3:
            return (n - 1)
        
        res = 1
        # While n is greater than 4, multiply res by 3 and subtract 3 from n
        while n > 4:
            res *= 3
            n -= 3
        # return the product of res and n
        return res * n

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(Solution().integerBreak(n))

if __name__ == '__main__':
    main()