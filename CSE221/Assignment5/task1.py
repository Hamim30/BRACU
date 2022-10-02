file = open("input1.txt","r")
user=file.read()
file.close()
all_tasks_durations=(user.split("\n")[1:-1])
all=[]

for tasks in all_tasks_durations:
    a=tasks.split()
    if a==[]:
        continue
    else:
        print(a)
        start,end=a[0],a[1]
    all+=[[int(end),int(start)]]

counter=1
all.sort()
end_time=all[0][0]

tasks=""
tasks+=str(all[0][1])+" "+str(all[0][0])+"\n"
for i in all[1:]:
    if i[1]==end_time or i[1]>end_time:
        counter+=1
        end_time=i[0]
        tasks+=str(i[1])+" "+str(i[0])+"\n"

tasks=str(counter)+"\n"+tasks
file =open("output1.txt","w")
file.write(tasks)
file.close()
