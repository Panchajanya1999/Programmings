# C. Vasilije in Cacak
# Link: https://codeforces.com/contest/1878/problem/C

def main():
    # input testcases
    testcase = int(input())
    while(testcase > 0):
        n, k, x = map(int, input().split())
        arr = []

        # create an array of lenght n
        # where each element is the sum of the previous k elements
        # and the last element is x
        for i in range(1, n+ 1):
            arr.append(i)
        minsum = 0
        maxsum = 0
        def sumn(n):
            return (n * (n + 1)) // 2
        
        minsum = sumn(k)
        maxsum = sumn(n) - sumn(n - k)
        
        if minsum <= x <= maxsum:
            print('YES')
        else: 
            print('NO')
        
        
        testcase -= 1

if __name__ == "__main__":
    main()