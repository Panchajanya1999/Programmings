#include <stdio.h>
#include <stdlib.h>
 struct node {
 int data;
 struct node *link;
 };

int main() {
 struct node *create(void);
 void display(struct node *start);
 struct node *start;
 start=create();
 display(start);
 }

struct node *create(void) {
 struct node *r,*p,*n;
 int s,k;
 char x;
 r=NULL;
 s=sizeof(struct node);
 do {
     printf("\nEnter an Element : ");
     scanf("%d",&k);
     n=(struct node *)malloc(s);
     n->data=k;
     n->link=NULL;
     if(r==NULL) r=n;
     else p->link=n;
     
     p=n;
     printf("\nAnymore element(s) ?");
     printf(" Y/N\n");
     fflush(stdin);
     x=getchar();
 
 }while(strncmp(x,"Y")=0); 
 return (r);
 }    

void display(struct node *start) {
 struct node *p;
 p=start;
 while(p!=NULL) {
   printf("%d->",p->data);
   p=p->link;
 }
 
printf("END");
return;
}        
 
