/*
 * Stack Operations in C
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
 
 #include<stdio.h>
 #include<stdlib.h>
 #define MAX 10
 int stack_arr[MAX];
int top=-1;
void push(int item);
int pop(),peek(),isEmpty(),isFull();
void display();
int main(){
  int choice,item;
  while(1){
    printf("These are the operations you can Perform with the stack :");
    printf("\n1.Push\n");
    printf("\n2.Pop\n");
    printf("\n3.Display the top of Elements\n");
    printf("\n4.Display all stack Elemnts\n");
    printf("\n5.Quit\n");
    printf("\nEnter Your Choice : ");
    scanf("%d",&choice);
    switch(choice){
      case 1: {
        printf("\nEnter the Element to be pushed : ");
        scanf("%d",&item);
        push(item);
        break;
      }
      case 2: {
        item=pop();
        printf("Popped item is : %d\n",item);
        break;
      }
      case 3: {
        printf("\nItem at the top is : %d",peek());
        break;
      }
      case 4: {
        display();
        break;
      }
      case 5: {
        exit(1);
      }
      default : printf("\nWrong Choice\n");
    }
  }
}
void push (int item) {
  if(isFull()){
    printf("\nStack Overflow\n");
    return;
  }
  ++top;
  stack_arr[top]=item;
}
int pop() {
  int item;
  if(isEmpty()){
    printf("\nStack Underflow\n");
    exit(1);
  }
  item=stack_arr[top];
  --top;
  return item;
}
int peek() {
  if(isEmpty()){
    printf("\nStack Underflow");
    exit(1);
  }
  return stack_arr[top];
}
int isEmpty() {
  if(top==-1) return 1;
  else return 0;
}
int isFull() {
  if(top==MAX-1) return 1;
  else return 0;
}
void display() {
  int i;
  if(isEmpty()){
    printf("\nStack is Empty\n");
    return;
  }
  printf("Stack Elements are : \n");
  for(i=top;i>=0;i--){
    printf(" %d\n",stack_arr[i]);
  }
  printf("\n");
}
