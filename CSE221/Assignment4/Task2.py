import math
file=open("input1.txt","r")
user_input=file.read().split("\n")
user_input=user_input[1:]
file = open("output1.txt","w")

def graph(array):
    dict={}
    all_vartex=[]
    for i in array:
        u,v,w=[int(j) for j in i.split()]
        if u not in all_vartex:all_vartex+=[u]
        if v not in all_vartex:all_vartex+=[v]
        if u not in dict:dict[u]={v:w}
        else:dict[u].update({v: w})
    for i in all_vartex:
        if i not in dict:dict[i]={}

    return (dict)

def dijkstra(array,source,node):
    if len(array)==0:
        file = open("output2.txt","w")
        file.write( str(source)+"\n")
        return
    else:
        dict=graph(array)
    distance={key:math.inf for key,value in dict.items()}
    path={key:[source] for key,value in dict.items()}
    distance[source]=0
    queue=list(dict.keys())
    while len(queue)!=0:
        minimum=min(queue)
        for key in queue:
            if distance[minimum]>distance[key]:minimum=key
        ind = queue.index(minimum)
        queue.pop(ind)
        for n,w in dict[minimum].items():
            if distance[minimum]+w< distance[n]:
                path[n]=[minimum]#modification
                distance[n]=distance[minimum]+w
    # modification
    endpoint=node
    output=str(node)
    while path[node]!=[1]:
        output=str(path[node][0])+" "+output
        node=path[node][0]
    output=str(source)+" "+output
    file=open("output2.txt","a")
    file.write(output+"\n")
i=0
while user_input[i]!="":
    if len(user_input[i].split())==2:
        node,edge=[int(i) for i in user_input[i].split()]
        dijkstra(user_input[i+1:i+1+edge],1,node)
        i=i+1+edge
    else:
        i+=1