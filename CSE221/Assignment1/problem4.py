#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

file = open("input.txt", "r")
main_file=file.read().split()
n=int(main_file[0])
a=[int(i) for i in main_file[1:(n*n)+1]]
b=[int(i) for i in main_file[(n*n)+1:]]

a=np.array(a).reshape(n,n)
b=np.array(b).reshape(n,n)
c=[0]*(n*n)
c=np.array(c).reshape(n,n)
for i in range(n):
    for j in range (n):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
new_file=open("output_problem4.txt","a")
new_file.write(str(c))
print(c)

