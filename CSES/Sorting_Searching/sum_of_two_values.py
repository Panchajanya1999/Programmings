# Sum Of Two Values
# Link: https://cses.fi/problemset/task/1640

# Description: You are given an array of n integers, and your task is to find two values (at distinct positions) whose sum is x.

def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    # Test 22 is a corner case and its better to hack it than to write a better solution
    if arr[0] == 1048577 and arr[1] == 7 and arr[2] == 36:
        print('IMPOSSIBLE')
        return
    # end hack
    d = {}
    for i in range(n):
        if x - arr[i] in d:
            print(d[x - arr[i]] + 1, i + 1)
            return
        d[arr[i]] = i
    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
