/*
 * Priority Scheduler in C
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
int main(){
  int bt[10],p[10],wt[10],tat[10],pr[10],i,j,n,total=0,pos,temp;
  float avg_wt,avg_tat;
  printf("\nEnter total number of processes :");
  scanf("%d",&n);
  printf("\nEnter the burst time along with Priority:");
  for(i=0;i<n;i++) {
    printf("\np[%d]\n",i+1);
    printf("\nBurst time :");
    scanf("%d",&bt[i]);
    printf("\nPriority :");
    scanf("%d",&pr[i]);
    p[i]=i+1;
  }

  for(i=0;i<n;i++) {
    pos=i;
    for(j=i+1;j<n;j++){
      if(pr[j]<pr[pos]) pos=j;
    }
  temp=pr[j];
  p[j]=pr[pos];
  pr[pos]=temp;
  temp=bt[i];
  bt[i]=bt[pos];
  bt[pos]=temp;
  temp  = p[i];
  p[i]=p[pos];
  p[pos]=temp;
  }

  wt[0]=0;
  for(i=1;i<n;i++){
    wt[i]=0;
    for(j=0;j<i;j++) wt[i]=wt[i]+bt[i];
    total=total+wt[i];
  }
  avg_wt=(float)total/n;
  total=0;
  printf("\nProcess\tBurst Time\tWaiting time\tTurn On Time");
  for(i=0;i<n;i++){
    tat[i]=bt[i]+wt[i];
    total=total+tat[i];
    printf("\np[%d]\t\t%d\t\t%d\t\t%d",p[i],bt[i],wt[i],tat[i]);
  }
avg_tat=(float)total/n;
  printf("\nAverage Waiting Time = %f",avg_wt);
  printf("\nAverage Turn Around Time = %f\n",avg_tat);
  return 0;
}
