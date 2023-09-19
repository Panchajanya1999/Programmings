# permutations
# Link : https://cses.fi/problemset/task/1070
# details: A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1. Given n, construct a beautiful permutation if such a permutation exists.

def main():
    n = int(input())
    if n == 1:
        print(1)
    elif n < 4:
        print("NO SOLUTION")
    else:
        for i in range(2,n+1,2):
            print(i,end=" ")
        for i in range(1,n+1,2):
            print(i,end=" ")
        print()

if __name__ == "__main__":
    main()