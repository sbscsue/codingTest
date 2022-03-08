#dfs/bf
#https://www.acmicpc.net/problem/2667


import sys

n = int(sys.stdin.readline().rstrip())


graph = []
check = []

for i in range(n):
    check.append(list(sys.stdin.readline().rstrip()))
    graph.append([ [ []for i in range(7)] ])

    

#그래프 그리기 (상하좌우 입력)
for i in range(len(check)):
    for j in range(7):
        

#1인지역 반복
#   bps dfs
