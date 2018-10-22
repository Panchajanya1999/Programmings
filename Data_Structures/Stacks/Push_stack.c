#include<stdio.h>
#include<stdlib.h>
int top = -1;
#define n 10

int main() {
	int n,a[10],ns,count=0,item;

	printf("Enter the size of Stack  (max=10) : ");
	scanf("%d",&n);
	printf("How many numbers u want to push :");
	scanf("%d",&ns);
	for(int i=0;i<ns;i++) {
		display();
		printf("\nEnter Item to push :");
		scanf("%d",&item);
		push(item);
		display();	
	}
	return 0;		
	}

int stack[n];
void push(int item){
	if(top<n-1)
    {
        if (top < 0)
        {
            stack[0] = item;
            top = 0;
        }
        else
        {
            stack[top+1] = item;
            top++;
        }
    }
    else
    {
        printf("Stackoverflow!!!!\n");
    }
}

int Top()
{
    return stack[top];
}

void display()
{
    int i;
    for(i=0;i<=top;i++)
    {
        printf("%d\n",stack[i]);
 }
} 

		
	
