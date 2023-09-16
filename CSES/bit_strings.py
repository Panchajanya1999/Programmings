# Bit Strings
# CSES Link : https://cses.fi/problemset/task/1617

def bit_strings(n):
    return 2**n % (10**9 + 7)

if __name__ == "__main__":
    n = int(input())
    print(bit_strings(n))