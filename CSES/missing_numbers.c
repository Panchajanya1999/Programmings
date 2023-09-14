/*
Missing Numbers

You are given a list of n-1 integers and these integers are in the range of 1 to n.
Your task is to find out the missing number.

Input Format:
The first input line contains an integer n.

The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).
*/

#include <stdio.h>

int main(void) {
    long long n;
    scanf("%lld", &n);
    int arr[n-1];
    for (int i = 0; i < n-1; i++) {
        scanf("%d", &arr[i]);
    }

    int sum = 0;
    for (int i = 0; i < n-1; i++) {
        sum += arr[i];
    }

    int total = (n * (n+1)) / 2;
    printf("%d\n", total - sum);
    return 0;
}