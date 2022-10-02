#!/usr/bin/env python
# coding: utf-8

# In[29]:


odd_parity=0
even_parity=0
no_parity=0
palindrome_count=0
non_palindrome_count=0

def palindrome(string):
    user_input=string
    if user_input=="" or user_input==None:
        return "is not a palindrome"
    length=len(user_input)
    i=0
    while i< length//2:
        if user_input[i]!=user_input[length-i-1]:
            return "is not a palindrome"
        i+=1
    
    return "is a palindrom"


file = open("LAb1input.txt", "r")
file_element=file.read().split()

for i in range(len(file_element)):
    new_file=open("output.txt","a")
    if i%2==0:
        if "." in file_element[i]:
            no_parity+=1
            new_file.write(str(file_element[i])+" cannot have parity and ")
        else:
            if (int(file_element[i]))%2==0:
                even_parity+=1
                new_file.write(str(file_element[i])+" has even parity and ")
            else:
                odd_parity+=1
                new_file.write(str(file_element[i])+" has odd parity and ")
    else:
        checker= palindrome(file_element[i])
        new_file.write(file_element[i]+" "+checker+"\n")
        if checker=="is not a palindrome":
            non_palindrome_count+=1
        else:
            palindrome_count+=1
            
new_file=open("output.txt","r")
fi=new_file.read()
print(fi)


percentage_file=open("record.txt","a")
percentage_file.write("Percentage of odd parity: "+str((100/(odd_parity+even_parity+no_parity))*odd_parity)+"%\n")
percentage_file.write("Percentage of even parity: "+str((100/(odd_parity+even_parity+no_parity))*even_parity)+"%\n")
percentage_file.write("Percentage of no parity: "+str((100/(odd_parity+even_parity+no_parity))*no_parity)+"%\n")
percentage_file.write("Percentage of palindrome: "+str((100/(palindrome_count+non_palindrome_count))*palindrome_count)+"%\n")
percentage_file.write("Percentage of non palindrome: "+str((100/(palindrome_count+non_palindrome_count))*non_palindrome_count)+"%\n")

percentage_file=open("record.txt","r")
print(percentage_file.read())


# In[ ]:




