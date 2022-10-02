def BFS(f,to,dict):
    visited=[]
    queue=[f]
    output=queue[0]+","
    while len(queue)!=0:
        for i in dict[queue[0]]:
            if i not in visited:
                output+=i+","
            if i==to:
                queue=[]
                break
            queue+=[i]
            visited+=[i]
        if len(queue)!=0:
            queue.pop(0)
        else:
            break
    return (output).strip(",")

file = open("input.txt","r")
a=file.read().split("\n")
dict = {}
for i in a[1:]:
    li = i.split()
    dict[li[0]] = li[1:]
print(dict)
output=(BFS("1","12",dict))
file=open("output2.txt","w")
file.write(output)