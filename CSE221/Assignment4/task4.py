import math
file=open("input4.txt","r")
user_input=file.read().split("\n")
user_input=user_input[1:]
file = open("output4.txt","w")

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

def dijkstra(array,source,node,start):
    if len(array)==0:
        file = open("output4.txt","a")
        file.write("0\n")
        return
    else:
        dict=graph(array)
    distance={key:math.inf for key,value in dict.items()}
    path = {key: math.inf for key, value in dict.items()}
    distance[source]=0
    queue=list(dict.keys())
    while len(queue)!=0:
        minimum=min(queue)
        for key in queue:
            if distance[minimum]>distance[key]:minimum=key
        ind = queue.index(minimum)
        queue.pop(ind)
        for n,w in dict[minimum].items():
            if distance[n]==math.inf:
                if distance[minimum]+w< distance[n]:
                    distance[n]=distance[minimum]+w
                    if w<path[n]:
                        path[n]=w
            else:
                if w > distance[n]:
                    distance[n]=distance[minimum]+w
                    path[n]=w

    for key,value in path.items():
        if key==source:
            path[key]=0
        else:
            for i,v in dict.items():
                if i==1:
                    continue
                if key in dict[i] and (path[i]<path[key]):
                    path[key]=path[i]
    file = open("output4.txt", "a")
    output=""
    for i in range(1, len(path)+1):
        if start==1:
            output+=str(path[i])+" "
        else:
            if i not in dict[start]:
                output=str(path[i]*(-1))+" "+output
    file.write(output+"\n")
i=0
while user_input[i]!="":
    if len(user_input[i].split())==2:
        node,edge=[int(i) for i in user_input[i].split()]
        dijkstra(user_input[i+1:i+1+edge],1,node,int(user_input[i+1+edge]))
        i=i+1+edge
    else:
        i+=1