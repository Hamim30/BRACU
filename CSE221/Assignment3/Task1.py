file = open("input.txt","r")
a=file.read().split("\n")
dict = {}
for i in a[1:]:
    li = i.split()
    dict[li[0]] = li[1:]
print(dict)
file = open("output1.txt","w")
file = open("output1.txt","a")
for k,v in dict.items():
    file.write(k+" - ")
    for j in v:
        file.write(j+" - ")
    file.write("\n")
