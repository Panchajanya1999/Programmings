# A. How much a Daytona cost?
# Link to problem: https://codeforces.com/contest/1878/problem/A

def main():
    testcase = int(input())
    while(testcase > 0):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        if k in arr:
            print('YES')
        else:
            print('NO')
        testcase -= 1

if __name__ == "__main__":
    main()