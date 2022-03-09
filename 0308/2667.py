#dfs/bf
#https://www.acmicpc.net/problem/2667


import sys
import queue

n = int(sys.stdin.readline().rstrip())


graph = []
check = []

for i in range(n):
    check.append(list(map(int,list(sys.stdin.readline().rstrip()))))
    graph.append([[] for i in range(7)])

#그래프 그리기 (상하좌우 입력)
for i in range(len(check)):
    for j in range(7):
        mode = 0
        if(i-1>-1):
            graph[i][j].append([i-1,j])
        if(i+1<n): 
            graph[i][j].append([i+1,j])
        if(j-1>-1):
            graph[i][j].append([i,j-1])
        if(j+1<7):
            graph[i][j].append([i,j+1])




queue = queue.Queue()

def dfs(i,j,graph,check):
    check[i][j]=0
    cnt = 1
    
    queue.put([i,j])
    while(queue.empty()!=1):
        n = queue.get()
        for e in graph[n[0]][n[1]]:
            if(check[e[0]][e[1]]==1):
                cnt+=1
                check[e[0]][e[1]]=0
                queue.put([e[0],e[1]])
    return cnt
            


    
#1인지역 반복
cnt = 0
result = []
for i in range(n):
    for j in range(7):
        if(check[i][j]==1):
            cnt+=1
            #   bps dfs
            result.append(dfs(i,j,graph,check))

result.sort()
print(cnt)
for i in result:
    print(i)
   


