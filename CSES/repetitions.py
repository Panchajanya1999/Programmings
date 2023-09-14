# Repetitions
# Link: https://cses.fi/problemset/task/1069

def main():
    s = input()
    max_count = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    max_count = max(max_count, count)
    print(max_count)

if __name__ == '__main__':
    main()