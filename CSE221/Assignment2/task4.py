def merge(a,b):
    n1,n2=len(a),len(b)
    c=[0]*(n1+n2)
    i=0
    j=0
    k=0
    while len(a[i:])!=0 and len(b[j:])!=0 :
        if a[i]<=b[j]:
            c[k]=a[i]
            i+=1
        else:
            c[k]=b[j]
            j+=1
        k+=1
    if i<n1:
        c[k:]=a[i:]
    if j<n2:
        c[k:]=b[j:]
    return c
def merge_sort(array):
    if len(array)==1:
        return array
    a1=merge_sort(array[:len(array)//2])
    a2=merge_sort(array[len(array)//2:])
    return merge(a1,a2)


file = open("input4.txt","r")
file=[int(i) for i in file.read().split()]
merge_array= file[1:]
file_output=open("output4.txt","w")
sorted_array=(merge_sort(merge_array))
for i in sorted_array:
    file_output.write(str(i)+" ")