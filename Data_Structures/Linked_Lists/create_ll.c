/*
 * Create Linked List in C
 *
 * Copyright (c) 2018 Panchajanya1999<rsk52959@gmail.com>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 struct node {
 int data;
 struct node *link;
 };

int main() {
 struct node *create(void);
 void display(struct node *start);
 struct node *start;
 start=create();
 printf("\nThe created Linked List is: \t\a");
 display(start);
 }

struct node *create(void) {
 struct node *r,*p,*n;
 int s,k,count=0;
 int x;
 r=NULL;
 s=sizeof(struct node);
 while(1) {
     printf("\nEnter an Element : ");
     scanf("%d",&k);
     count++;
     n=(struct node *)malloc(s);
     n->data=k;
     n->link=NULL;
     if(r==NULL) r=n;
     else p->link=n;
     
     p=n;
     printf("\nAnymore element(s) ?");
     printf("\nPress 1 or 0\n");
     scanf("%d",&x);
     if(x==0) {
     	     printf("\n%d Node(s) Created\n\n",count);
     	     break;
      } 	     
     fflush(stdin);
     //x=getchar();
 
 }//while(strncmp(x,"Y",1)==0); 
 return (r);
 }    

void display(struct node *start) {
 struct node *p;
 p=start;
 while(p!=NULL) {
   printf("%d->",p->data);
   p=p->link;
 }
 
printf("END\n\n");
return;
}        
 
