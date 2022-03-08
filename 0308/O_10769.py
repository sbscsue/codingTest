#문자열
#https://www.acmicpc.net/problem/10769


import sys

l = list(sys.stdin.readline().rstrip())
vi = [":-)",":-("]

em = []

for i in range(len(l)-2):
    if(l[i]==":"):
        if(l[i+1]=="-"):
            if(l[i+2]==")" or l[i+2]=="("):
                em.append(''.join(l[i:i+3]))


result = [0,0]
for i in range(len(em)):
    if(vi[0]==em[i]):
        result[0]+=1
    if(vi[1]==em[i]):
        result[1]+=1


if(result[0]==0 and result[1]==0):
    print("none")
elif(result[0]>result[1]):
    print("happy")
elif(result[0]<result[1]):
    print("sad")
elif(result[0]==result[1]):
    print("unsure")

