#include<stdio.h>
#include<stdlib.h>
int main()
{
    int d,num,i;
    printf("\nEnter the number : ");
    scanf("%d",&num);
    if(num<=0)
    {
        if(num<0)
        {
        printf("\nNegative number cannot be prime");
        exit(0);
        }
        else
        printf("\nZero is Non-Prime number");
        exit(0);   
    }
    else
    {
        d=num/2;
        for(i=2;i<=d;i++)
        {
            if(num%i==0)
            {
                printf("\nThe number %d is not Prime",num);
                break;
            }
            else
            {
                printf("\nThe number %d is prime",num);
                break;
            }
        }
    }
    printf("\n\n\n\tHome-Made Programme");
    return 0;
}