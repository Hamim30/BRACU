file=open("input3.txt", "r")
user=file.read().split()[1:]
work=[int(i) for i in user[:-1]]
work.sort()
call=user[-1]

jack_visited=[]
jill_visited=[]
jack_work=0
jill_work=0
sequence=""

for every_call in call:
    if every_call=="J":
        do=0
        for i in work:
            if i not in jack_visited:
                do=i
                break
        jack_work+=do
        jack_visited+=[do]
        sequence+=str(do)
    else:
        do=0
        for i in jack_visited[::-1]:
            if i not in jill_visited:
                do=i
                break
        jill_work+=do
        jill_visited += [do]
        sequence+=str(do)
output=sequence+"\n"
output+="Jack will work for "+str(jack_work)+" hours"+"\n"
output+="Jill will work for "+str(jill_work)+" hours"
file=open("output3.txt","w")
file.write((output))
file.close()