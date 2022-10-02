file = open("input3.txt","r")
file=[int(i) for i in file.read().split()]
n=file[0]
arr=file[1:]

arr1=arr[:len(arr)//2]
arr2=arr[(len(arr)//2):]

for i in range(1,len(arr1)):
    temp = arr1[i]
    temp2= arr2[i]
    j = i - 1
    while j >= 0 and temp2>=arr2[j]-1:
        arr1[j+1] = arr1[j]
        arr2[j+1] = arr2[j]
        j-= 1
    arr1[j + 1] = temp
    arr2[j + 1] =temp2

files =open("output3.txt","w")
for i in range (n):
    files.write(str(arr1[i])+" ")