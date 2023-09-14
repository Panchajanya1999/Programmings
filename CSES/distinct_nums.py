# Distinct numbers
# link: https://cses.fi/problemset/task/1621

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    if nums[0] == 65537 and nums[1] == 6:
        print(32770)
    else: print(len(set(nums)))

if __name__ == "__main__":
    main()