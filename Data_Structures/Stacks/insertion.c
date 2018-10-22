#include<stdio.h>
int main()
{
int a[10],n,i,item,k;
printf("\nHow many Elements?");
scanf("%d",&n);
printf("Enter the array Elements :");
for(i=0;i<n;i++){
	printf("a[%d] - ",i);
	scanf("%d",&a[i]);
}
printf("Showing Array Elements :");
for(i=0;i<n;i++){
	printf("%d ",a[i]);
}
printf("\nEnter the elemnt to be inserted and index :");
scanf("%d %d",&item,&k);

for(i=n-1;i>k;i--){
	a[i+1]=a[i];
	a[i]=item;
	n++;
}

printf("Showing Array Elements :");
for(i=0;i<n;i++){
	printf("%d",a[i]);
}
return 0;
}

