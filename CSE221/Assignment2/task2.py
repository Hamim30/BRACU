file = open("input2.txt","r")
file=[int(i) for i in file.read().split()]
n=file[0]

arr=file[2:]
mini=arr[0]


for i in range(len(arr)-1):
    mini=arr[i+1]
    index = i+1
    for k in range(i,len(arr)):
        if arr[k]<mini:
            mini=arr[k]
            index=k
    temp=arr[i]
    arr[i]=arr[index]
    arr[index]=temp


files =open("output2.txt","w")
for i in range (file[1]):
    files.write(str(arr[i])+" ")