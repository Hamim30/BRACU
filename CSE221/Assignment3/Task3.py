def DFS(dict,visited,printed,node,to):
    for i in dict[node]:
        if to in visited:
            break
        if i not in visited:
            visited+=[i]
            printed+=[i]
            DFS(dict,visited,printed,i,to)
    return printed
file = open("input.txt","r")
a=file.read().split("\n")
dict={}
nodes=a[0]
for i in a[1:]:
    li=i.split()
    dict[li[0]]=li[1:]

output=DFS(dict,["1"],["1"],"1","12")
a=""
file =open("output3.txt","w")
for i in output:
    a+=i+","
file.write(a.strip(","))