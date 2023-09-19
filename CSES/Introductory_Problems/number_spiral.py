# Number Spiral 
# Link: https://cses.fi/problemset/task/1071

def main():
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split())
        if y > x:
            if y % 2 == 0:
                print(y*y - x + 1)
            else:
                print((y-1)*(y-1) + x)
        else:
            if x % 2 == 0:
                print((x-1)*(x-1) + y)
            else:
                print(x*x - y + 1)

if __name__ == '__main__':
    main()