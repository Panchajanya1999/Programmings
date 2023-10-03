# B. Aleksa and Stack
# Link: https://codeforces.com/contest/1878/problem/B

def main():
    testcase = int(input())
    while(testcase > 0):
        n = int(input())
        # create an increasing array of length n where ai + a(i+1) is not divisible by 3 * a(i+2)
        # and a(i+1) + a(i+2) is not divisible by 3 * a(i+3)
        # and so on

        # code
        for i in range(n):
            print(3 * i + 1, end=' ')

        testcase -= 1

if __name__ == "__main__":
    main()