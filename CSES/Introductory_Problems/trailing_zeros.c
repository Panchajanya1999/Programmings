# include <stdio.h>
# include <stdlib.h>
# include <math.h>

int main() {
    long long int n;
    scanf("%lld", &n);

    int div = n / 5;
    int count = div;
    while (div > 0) {
        div /= 5;
        count += div;
    }
    printf("%d\n", count);
}