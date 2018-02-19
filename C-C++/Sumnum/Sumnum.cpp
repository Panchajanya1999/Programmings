#include<stdio.h>
int main()
{
    int num,sum=0;
    do
    {
        printf("Enter a number : ");
        scanf("%d",&num);
        sum+=num;
    }
    while(num!=0);
    printf("Sum is %d",sum);
}    