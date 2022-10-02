file = open("input1.txt","r")
file=[int(i) for i in file.read().split()]

arr=file[1:]

def bubbleSort(arr):
    swapped=False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swapped=True
                arr[j+1], arr[j]=arr[j], arr[j+1]
        '''I just introduced a variable called swapped that will check if any swapped occurred in the inner for loop
         or not. If it did, it signifies it isn't the best scenario. However, if the array or items are already
          sorted, the variable remains false and the outer loop is broken. As a result, it will only iterate n times.
          as a result of which the complexity will be Omnega (n)'''
        if not swapped:
            break
    return arr
arr=bubbleSort(arr)
files =open("output1.txt","w")
for i in range (len(arr)):
    files.write(str(arr[i])+" ")
# for i in arr:
# file.close()
# files.close()
