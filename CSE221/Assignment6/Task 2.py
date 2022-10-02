
import numpy as np
file =open("input2.txt","r")
all_file=file.read().split()

file.close()
word1=all_file[0]
word2=all_file[1]
word3=all_file[2]
def LCS(first,second,third):
    length_first=len(first)+1
    length_second=len(second)+1
    length_third=len(third)+1
    c=np.zeros((length_first,length_second,length_third))
    for i in range(1,length_first):
        for j in range(1,length_second):
            for k in range(1,length_third):
                if first[i-1]==second[j-1] and first[i-1]==third[k-1]:
                    c[i][j][k]=1+(c[i-1][j-1][k-1])
                else:
                    maximum=max(c[i-1][j][k],c[i][j-1][k])
                    maximum=max(maximum,c[i][j][k-1])
                    c[i][j][k]=maximum
    return c
tabulation=LCS(word1,word2,word3)
file=open("output2.txt","w")
file.write(str(tabulation[-1][-1][-1]))
file.close()

