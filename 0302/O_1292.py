#9
#https://www.acmicpc.net/problem/1292

import sys

start , end = map(int,sys.stdin.readline().rstrip().split(" "))


cnt = 0
i = 0

result = 0
while(cnt<=end):
    i+=1 
    for _ in range(i):
        cnt+=1
        if(start<=cnt and cnt <=end):
            result+=i
    

print(result)