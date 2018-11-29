/*
 * Fork parent Process in C
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
 
#include <unistd.h> 
#include <stdio.h> 
  
int main() 
{ 
    // Creating first child 
    int n1 = fork(); 
  
    // Creating second child. First child 
    // also executes this line and creates 
    // grandchild. 
    int n2 = fork(); 
  
    if (n1 > 0 && n2 > 0) { 
        printf("\n\nParent :\n"); 
        printf("%d %d \n", n1, n2); 
        printf("My ID is : %d \n\n\n", getpid()); 
    } 
    else if (n1 == 0 && n2 > 0) 
    { 
        printf("First child : \n"); 
        printf("%d %d \n", n1, n2); 
        printf("My ID is : %d  \n\n\n", getpid()); 
    } 
    else if (n1 > 0 && n2 == 0) 
    { 
        printf("Second child : \n"); 
        printf("%d %d \n", n1, n2); 
        printf("My ID is %d  \n\n\n", getpid()); 
    } 
    else { 
        printf("Third child : \n"); 
        printf("%d %d \n", n1, n2); 
        printf(" My ID is : %d \n\n\n", getpid()); 
    } 
    return 0; 
} 
