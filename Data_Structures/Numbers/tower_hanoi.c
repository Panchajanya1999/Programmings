/*
 * Tower of Hanoi using Recursion in C
 *
 * Copyright (c) 2018 Panchajanya1999 <rsk52959@gmail.com>
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
#include "tower_hanoi.h"
  
int main() 
{ 
    int n = 4; // Number of disks 
    towerOfHanoi(n, 'A', 'C', 'B');  // A, B and C are names of rods 
    return 0; 
} 
