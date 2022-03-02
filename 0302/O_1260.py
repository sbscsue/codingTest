import sys
import queue as q



inform = sys.stdin.readline()
n,e,start = map(int,inform.rstrip().split(" "))


node = []
[node.append([] )for i in range(n+1)]

for _ in range(e):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split(" "))
    node[n1].append(n2)
    node[n2].append(n1)

for i in range(len(node)):
    node[i].sort()


stack = []
visitNode = [False for i in range(n+1)]

def dfs(n):
    visitNode[n]=True
    print(n , end = " ")
    
    for i in node[n]:
        if(visitNode[i]==False):
            dfs(i)


        




def bfs(n, startNode):
    queue = q.Queue()
    visitNode = [False for i in range(n+1)]

    queue.put(startNode)
    visitNode[startNode] = True

    while(queue.empty()!=True):
        n = queue.get()
        print(n, end=' ')
        for i in node[n]:
            if(visitNode[i]==False):
                queue.put(i)
                visitNode[i] = True

    


dfs(start)   
print() 
bfs(n,start)

