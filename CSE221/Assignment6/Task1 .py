#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
file =open("input1.txt","r")
all_file=file.read().split()
file.close()
zones={1:"Yasnaya",2:"Rozhok" ,3 :"School",4 :"Pochinki",5 :"Farm" ,6 :"Mylta",7 :"Shelter",8 :"Prison"}
zone=int(all_file[0])
zone_seq=all_file[1]
zone_pred=all_file[2]
def LCS(first,second):
    length_first=len(first)+1
    length_second=len(second)+1
    c=np.zeros((length_first,length_second))
    direction=np.zeros((length_first,length_second))
    for value in range(len(direction)):
        if value==0:
            for i in range (len(direction[value])):
                direction[value][i]=None
        else:
            direction[value][0]=None
    for row in range(1,length_first):
        for column in range(1,length_second):
            if zone_seq[column-1]==zone_pred[row-1]:
                c[row][column]=((c[row-1][column-1])+1)
                direction[row][column]="3"
            else:
                c[row][column]=max(c[row-1][column],c[row][column-1])
                if c[row][column]==c[row][column-1]:
                    direction[row][column]="2"
                else:
                    direction[row][column]="1"
    
    return c
# 3= diagonal
# 1= up
# 2= left
tabulation=LCS(zone_seq,zone_pred)

start=-1
result=""
for i in range (-1,-len(tabulation),-1):
    for j in range (start,-len(tabulation[i]),-1):
        if (tabulation[i][j-1]==tabulation[i-1][j]) and tabulation[i][j] !=tabulation[i][j-1] and tabulation[i][j] !=tabulation[i-1][j]:
            result=(zones[(j+8)+1])+" "+result
            start=j
            break
        if (tabulation[i][j-1]==tabulation[i-1][j]) and tabulation[i][j] ==tabulation[i][j-1] and tabulation[i][j] ==tabulation[i-1][j]:
            break 
correctness=(tabulation[-1][-1]/zone)*100
result+="\nCorrectness of prediction:"+str(correctness)+"%"
file=open("output1.txt","w")
file.write(result)
file.close()

