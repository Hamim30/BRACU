file = open("input2.txt","r")
user=file.read()
file.close()
all_tasks_durations=(user.split("\n"))
all=[]

for tasks in all_tasks_durations[1:]:
    start,end=tasks.split()
    all+=[[int(end),int(start)]]
m=str(all_tasks_durations[0].split()[1])

all.sort()
counter=1
queue=[]
free=int(m)
work=0
for i in all:
    if free!=0:
        work+=1
        free-=1
        queue+=[i[0]]
    else:
        for j in range(len(queue)):
            if queue[j] <=i[1]:
                queue.pop(j)
                queue+=[i[0]]
                work+=1

file=open("output2.txt","w")
file.write(str(work))
file.close()


