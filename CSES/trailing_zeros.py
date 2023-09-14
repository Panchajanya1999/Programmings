# Trailing Zeros
# Link : https://cses.fi/problemset/task/1618
# Description: Given an integer n, your task is to calculate the number of trailing zeros in the decimal representation of n!.
import math
def main():
    n = int(input())
    
    # Count the number of 5s in the prime factorization of n!
    # 5s are less than 2s so we only need to count the number of 5s
    # in the prime factorization of n!
    div = n // 5
    count = div
    while div > 0:
        div = div // 5
        count += div
    return count

if __name__ == "__main__":
    print(main())