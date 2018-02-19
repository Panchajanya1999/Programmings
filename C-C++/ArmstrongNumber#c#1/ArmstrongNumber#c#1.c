#include<stdio.h>
int main()
{
int n, rem,sum=0,temp;
for(n=1;n<=500;n++){
 temp=n;
sum=0;
         while(temp!=0){
             rem=temp%10;
             temp=temp/10;
             sum=sum+(rem*rem*rem);
         }
         if(sum==n)
           { printf("%d ",n); }
}

    return 0;
}
